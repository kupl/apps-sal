import sys


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


MOD = 998244353
(N, S) = lr()
A = lr()
dp = [0] * (S + 1)
answer = 0
for a in A:
    dp[0] += 1
    prev = dp.copy()
    for i in range(S - a + 1):
        dp[i + a] += prev[i]
    answer += dp[-1]
print(answer % MOD)
