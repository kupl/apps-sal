(N, K) = map(int, input().split())
mod = 998244353
L = list()
R = list()
for i in range(K):
    (l, r) = map(int, input().split())
    L.append(l)
    R.append(r)
dp = [0] * (N + 1)
dp[1] = 1
dpSum = [0] * (N + 1)
dpSum[1] = 1
for i in range(2, N + 1, 1):
    for j in range(K):
        li = i - R[j]
        ri = i - L[j]
        if ri < 0:
            continue
        li = max(li, 1)
        dp[i] += dpSum[ri] % mod - dpSum[li - 1] % mod
    dpSum[i] = dpSum[i - 1] % mod + dp[i] % mod
ans = dp[N]
print(ans % mod)
