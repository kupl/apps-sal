N, K = map(int, input().split())
mod = 998244353
dp = [0] * (N + 1)
R = []
L = []
for i in range(K):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

dp[1] = 1
s = [0] * (N + 1)
s[1] = 1
for i in range(2, N + 1, 1):
    for j in range(K):
        li = i - R[j]
        ri = i - L[j]
        if ri < 1:
            continue
        li = max(li, 1)
        dp[i] += s[ri] % mod - s[li - 1] % mod
    s[i] = s[i - 1] % mod + dp[i] % mod
ans = dp[N] % mod
print(ans)
