from math import ceil
N, D, A = list(map(int, input().split()))
P = []
for _ in range(N):
    P.append(list(map(int, input().split())))
    # X,H

P.sort()

# for p in P:
#  print(p)

# Attack[i] : i番目（Xi）を左端に爆弾を投げたとき、巻き込める最大の番号Xj
Attack = [-1 for _ in range(N)]
leftx, leftj = 0, 0
for i in range(N):
    now = P[i][0]
    leftx = now + 2 * D
    while leftj < N:
        if P[leftj][0] <= leftx:
            leftj += 1
        else:
            break
    Attack[i] = leftj - 1

# print(Attack)
# damage管理
# 範囲攻撃はimosっぽくやる。届いた左端に+Dして、届いた右端の右隣に-Dする
# 今までのダメージ総和をworkとして持ちつつ、imosで回復すればよい
wk_dam = 0
imos = [0] * (N + 1)
ans = 0
for i in range(N):
    wk_dam += imos[i]
    # print(i,wk_dam,P[i][1],ans)
    if P[i][1] <= wk_dam:
        # すでに累積ダメージで死んでる
        continue
    cnt = (P[i][1] - wk_dam + A - 1) // A  # ceil(zanHP / A)
    wk_dam += cnt * A
    imos[i] += cnt * A
    imos[Attack[i] + 1] -= cnt * A
    ans += cnt

print(ans)
# print(imos)
