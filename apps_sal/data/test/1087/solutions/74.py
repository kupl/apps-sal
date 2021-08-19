# D - XXOR

import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
A = list(int(x) for x in readline().split())

# bits[i] := i桁目に現れる"1"の和
bits = [0] * 50
for i in range(N):
    for j in range(50):
        if A[i] >> j & 1:
            bits[j] += 1

# dp[i][smaller] := 上から(49, 48, 47...)i桁目まで決めた時に、
# Kと同じように選んで行ったとき(smaller = 0)
# K以下となるように選んだとき(smaller = 1)
# のそれぞれの最大値とする
dp = [[0] * 2 for _ in range(50)]

for i in range(49)[::-1]:
    # 上から順にチェックする(49, 48, 47...2, 1, 0)
    check_bit = 1 << i
    # Kのi桁目が"1"のとき
    if K & check_bit:
        # XをK以下にする場合。
        # i桁目は"0"になるので、bits[i](*2^i)が得点になる。
        dp[i][1] = dp[i + 1][0] + (bits[i] * check_bit)
        # 一度smaller=1になったらsmaller=1にしか遷移しない。
        if dp[i + 1][1] != 0:
            dp[i][1] = max(dp[i][1], dp[i + 1][1] + (max(N - bits[i], bits[i]) * check_bit))
        # Kのi桁目"1"の通りにするので、i桁目が反転される。
        # つまり、元々"0"だった個数分が得点になる。
        dp[i][0] = dp[i + 1][0] + ((N - bits[i]) * check_bit)
    # Kのi桁目が"0"のとき
    else:
        # 一度smaller=1になったらsmaller=1にしか遷移しない。
        # 0か1かは最大値が大きくなる方を選べば良い。
        if dp[i + 1][1] != 0:
            dp[i][1] = dp[i + 1][1] + (max(N - bits[i], bits[i]) * check_bit)
        # Kのi桁目"0"の通りにするので、bits[i]が得点になる
        dp[i][0] = dp[i + 1][0] + (bits[i] * check_bit)

print(max(dp[0][0], dp[0][1]))
