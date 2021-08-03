# 辞書順最小、というのがポイント
# 最初は小さく進んであとから大きく進む。これは難しい。最初いくつにすれば上手くゴールできるのか不明だ。
# 最初は大きく進んであとから小さくするのはただの貪欲なので簡単。
# したがって、ゴールからスタートに向かって貪欲に逆に進めばよい

n, m = list(map(int, input().split()))
masu = list(input())

idx = n
ans = []

while True:
    valid = False
    next_min_idx = max(idx - m, 0)
    for candi in reversed(list(range(next_min_idx, idx))):
        if masu[candi] == '0':
            destination = candi
            valid = True
    if not valid:
        # mマス連続で1なので必ずゲームオーバー
        print((-1))
        return
    ans.append(idx - destination)
    idx = destination

    if idx == 0:
        break

str_list = list(map(str, ans))
print((' '.join(reversed(str_list))))
