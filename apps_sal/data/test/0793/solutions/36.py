from numpy import array, ones
mod = 10 ** 9 + 7
(N, M, *ST) = map(int, open(0).read().split())
(S, T) = (ST[:N], array(ST[N:]))
dp = ones(M + 1, dtype='int64')
for s in S:
    dp[1:] = ((dp[:-1] * (s == T)).cumsum() + dp[1:]) % mod
print(dp[-1])
