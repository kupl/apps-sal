import sys
readline = sys.stdin.readline
(N, M) = map(int, readline().split())
broken = set([int(readline()) for i in range(M)])
dp = [0] * (N + 1)
dp[0] = 1
if 1 not in broken:
    dp[1] = 1
DIV = 10 ** 9 + 7
for i in range(2, N + 1):
    if i in broken:
        continue
    dp[i] = dp[i - 2] + dp[i - 1]
    dp[i] %= DIV
print(dp[N])
