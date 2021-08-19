mod = 998244353
(N, *XD) = map(int, open(0).read().split())
XD = sorted(zip(*[iter(XD)] * 2), reverse=True)
S = [(10000000000.0, 0)]
dp = [1] + [0] * N
for (i, (x, d)) in enumerate(XD):
    j = i
    while S[-1][0] < x + d:
        (_, j) = S.pop()
    S.append((x, j))
    dp[i + 1] = (dp[i] + dp[j]) % mod
print(dp[-1])
