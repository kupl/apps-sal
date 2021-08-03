import itertools
import bisect


n, m = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]

# lとvの組を入力し、vの昇順でソート
l_v = []
for i in range(m):
    l_v.append([int(i) for i in input().split()])
l_v.sort(key=lambda x: (x[1]))

"""
lとvをそれぞれ分けて格納（後々vの値で二分探索したいので）
2頭のラクダが通れる橋を後々二分探索する
その時にlの累積maxであるmax_lを用いる
"""

l = []
v = []
max_l = []
max_l_ = 0

for i in range(m):
    l.append(l_v[i][0])
    v.append(l_v[i][1])
    max_l_ = max(l_v[i][0], max_l_)
    max_l.append(max_l_)

if min(v) < max(w):  # 一番重いラクダが一番弱い橋を通れない
    print(-1)
    return

"""
n頭の合計重さweightを耐えられない橋の中で最も距離が長い橋を記録する
2分探索で求めたindex（n頭のラクダの合計の重さを耐えられる端の中で最も強度が弱いもの）
より前のindexの橋（ラクダの重さを耐えられない橋）の中で最も距離が大きい橋の長さ
→max_lを使う！
"""

x = [0 for j in range(2**n)]
for i in itertools.product([0, 1], repeat=n):
    weight = sum([w[_] * i[_] for _ in range(n)])
    a = bisect.bisect_left(v, weight)
    if a >= 1:
        x[sum([2**k * i[k] for k in range(n)])] = max_l[a - 1]

"""
ラクダの並び方全n!の組合せにおいて、それぞれDPによって取らなければいけない距離を計算し、その最小値をansとする
"""
ans = float("inf")
for i in itertools.permutations([_ for _ in range(n)]):
    dp = [0 for _ in range(n - 1)]
    dp[0] = x[2 ** i[1] + 2 ** i[0]]
    for j in range(n - 2):
        if j == 0:
            dp[j + 1] = max(dp[j] + x[2 ** i[2] + 2 ** i[1]], x[2 ** i[2] + 2 ** i[1] + 2 ** i[0]])

        else:
            dpp = []
            for k in range(j + 1):
                # print(i,j, k, [i[j + 1 - kk] for kk in range(j+2-k)])
                sumbit = sum([2 ** i[j + 2 - kk] for kk in range(j + 2 - k)])
                dpp.append(dp[k] + x[sumbit])
            sumbit2 = sum([2 ** i[j + 2 - kk] for kk in range(j + 3)])
            dpp.append(x[sumbit2])
            dp[j + 1] = max(dpp)

    ans = min(ans, dp[-1])

print(ans)
