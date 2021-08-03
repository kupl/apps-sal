# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
#sys.stdin = open("input.txt", "r")
MOD = 10**9 + 7

n, m, k = map(int, input().split())
a = sorted(map(int, input().split()))
a = a[:k]
ps = [0]
for i in range(k):
    ps.append(ps[-1] + a[i])
bf = []
temp = [0 for i in range(k + 1)]
for i in range(m):
    b, f = map(int, input().split())
    if b <= k:
        temp[b] = max(temp[b], f)
for i in range(1, k + 1):
    if temp[i] != 0:
        bf.append((i, temp[i]))
bf = [(1, 0)] + sorted(bf, key=lambda x: (x[0] - x[1], b))

dp = [[-1 for i in range(len(bf))] for i in range(k + 1)]

for i in range(len(bf)):
    dp[0][i] = 0
for i in range(1, k + 1):
    dp[i][0] = ps[i]

for i in range(1, k + 1):
    for j in range(1, len(bf)):
        dp[i][j] = dp[i][j - 1]
        b = bf[j][0]
        f = bf[j][1]
        if b <= i:
            dp[i][j] = min(dp[i][j], dp[i - b][len(bf) - 1] + ps[i] - ps[i - b + f])

print(dp[k][len(bf) - 1])
