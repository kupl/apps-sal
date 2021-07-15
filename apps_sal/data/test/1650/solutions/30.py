import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

l = read().rstrip().decode()
n = len(l)
mod = 10 ** 9 + 7
dp = [[0, 0] for _ in range(n)]
dp[0] = [1, 2]
for i, check in enumerate(l[1:]):
    i += 1
    dp[i][0] = dp[i - 1][0] * 3
    dp[i][1] = dp[i - 1][1]
    if check == '1':
        dp[i][0] += dp[i - 1][1]
        dp[i][1] += dp[i - 1][1]
    dp[i][0] %= mod
    dp[i][1] %= mod
print((sum(dp[-1]) % mod))

