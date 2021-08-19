import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
mod = 998244353
a.sort()
dp = [1] + [0] * n
for i in range(1, n + 1):
    (x, pt) = (1, i - 2)
    while pt >= 0 and 2 * a[pt] > a[i - 1]:
        x = x * (n - pt - 2) % mod
        pt -= 1
    dp[i] = (dp[i - 1] * (n - i) + dp[pt + 1] * x) % mod
print(dp[-1])
