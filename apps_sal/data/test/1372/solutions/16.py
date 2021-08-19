import sys
h, n = list(map(int, input().split()))
# A = [0] * n
# B = [0] * n
# for i in range(n):
#     A[i], B[i] = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
min_hp = h
max_hp = h + max(a for a, b in (AB))

dp = [sys.maxsize] * (max_hp + 1)
dp[0] = 0

for i in range(1, max_hp + 1):
    # dp[i] = min(dp[i - A[j]] + B[j] for j in range(n))
    dp[i] = min(dp[i - a] + b for a, b in AB)
print((min(dp[h:])))
