"""
解説＆prd_xxxさん #17179888　から引用
基本方針:dpでOK,NGを判定しながら最後までOKいけたらYES
制約条件
start,endは違う人をペアにしてはいけない
同時に乗った人は、同じ階数を移動する
ある階では誰かが乗るor下りるのみ。
"""

import collections
N = int(input())
AB = [tuple(map(int, input().split())) for i in range(N)]
ctr = collections.defaultdict(int)
pairs = {}  # 乗降ともにわかっている
starts = set()  # 乗のみわかっている
ends = set()  # 降のみわかっている
for a, b in AB:
    if a > 0 and b > 0:  # 乗降ともにわかっている
        pairs[a] = b
        ctr[a] += 1
        ctr[b] += 1
    elif a > 0:  # 乗のみわかっている
        ctr[a] += 1
        starts.add(a)
    elif b > 0:  # 降のみわかっている
        ctr[b] += 1
        ends.add(b)
    else:  # どっちもわかんない
        continue

if any(v > 1 for v in list(ctr.values())):  # 重複チェック
    print('No')
    return

dp = [False] * (N + 1)  # 添え字はチェックし[終わった階/2]と思えばよい。区間は偶数のどこかで切れるのでN+1で管理できる 2階x N区間 + 初期1という意味。
dp[0] = True  # はじめはok
for i in range(N):  # iは確定した区切りの最終区間Noを示す引数　つぎのグループの最初に乗る人の階は2*i+1になる
    if not dp[i]:
        continue  # 確定した区間がfalse状態では、その後どうやってもTrueにできないからfalseのままチェックを終わらせる
    for j in range(i + 1, N + 1):  # jはi(確定した区切りの最終区間Noを示す引数)+1以降で乗ったグループの人が降りる区間終端を示す引数 　乗る区間をlとすると、i + l = j で管理される。
        if dp[j]:
            continue  # すでに成立済みならとばす
        l = j - i  # のる区間は乗る階数と同じ
        for s in range(2 * i + 1, 2 * i + l + 1):  # sは乗る階。i+1区間のはじめに乗る(2*i+1)階と その人が降りる2*i+l+1階の間の階は乗ってくるひとばかり。と仮定する
            t = s + l  # 各のってくるひとが下りる階
            if s in pairs:  # 乗る階がペアにある
                if pairs[s] != t:
                    break  # 乗る階と降りる階がペア制約に反するとダメ
            if s in starts and t in ends:
                break  # 乗る階、降りる階が、すでに確定している２人の条件とかぶるので制約に反してダメ。start,endは違う人をペアにしてはいけない
            if s in ends:
                break  # 乗る階が降りる階リストにあってもダメ
            if t in starts:
                break  # 降りる階が乗る階リストにあってもダメ
        else:
            dp[j] = True  # jまでの区間は矛盾がないことをメモ
print(('Yes' if dp[-1] else 'No'))  # 最後まで矛盾がなければYes
