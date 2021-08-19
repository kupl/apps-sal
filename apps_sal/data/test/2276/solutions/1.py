import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
s = input().strip()
a = [0] + list(map(int, input().split()))
MX = 105
dp = [0] * MX ** 3


def f(i, j, k):
    if i == j:
        return 0
    idx = i * MX * MX + j * MX + k
    if not dp[idx]:
        dp[idx] = f(i + 1, j, 1) + a[k]
        for m in range(i + 1, j):
            if s[i] == s[m]:
                dp[idx] = max(dp[idx], f(i + 1, m, 1) + f(m, j, k + 1))
    return dp[idx]


print(f(0, n, 1))
