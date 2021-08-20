import sys


def input():
    return sys.stdin.readline()[:-1]


(_, S) = list(map(int, input().split()))
mod = 998244353
ans = 0
dp = [0] * (S + 1)
for a in map(int, input().split()):
    dp[0] += 1
    for i in range(S, a - 1, -1):
        dp[i] += dp[i - a]
        dp[i] %= mod
    ans += dp[-1]
    ans %= mod
print(ans)
