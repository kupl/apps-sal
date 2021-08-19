(N, M) = map(int, input().split())
A = [True] * N
for _ in range(M):
    a = int(input())
    A[a - 1] = False
waru = 10 ** 9 + 7
dp = [0] * (N + 1)
(dp[0], dp[1]) = (1, 1)
if not A[0]:
    dp[1] = 0
for i in range(2, N + 1):
    if not A[i - 1]:
        dp[i] = 0
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % waru
print(dp[-1])
