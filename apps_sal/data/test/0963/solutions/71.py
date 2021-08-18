import sys
readline = sys.stdin.readline
read = sys.stdin.read


def get(i, l, r):
    a = i - r
    b = i - l
    if b < 0:
        return 0
    return acc[b] - (acc[a - 1] if a - 1 >= 0 else 0)


n, k = map(int, readline().split())
lr = [list(map(int, readline().split())) for _ in range(k)]

dp = [0] * (n)
dp[0] = 1
acc = [1] * (n)


MOD = 998244353
for i in range(1, n):
    v = 0
    for l, r in lr:
        v += get(i, l, r)
    dp[i] = v % MOD
    acc[i] = (acc[i - 1] + dp[i]) % MOD

print(dp[n - 1] % MOD)
