n, k = list(map(int, input().split()))
mod = 998244353
dp = [0 for _ in range(n + 5)]
dpsum = [0 for _ in range(n + 5)]
dp[1] = 1
dpsum[1] = 1
l = []
r = []

for i in range(k):
    ll, rr = list(map(int, input().split()))
    l.append(ll)
    r.append(rr)

for i in range(1, n + 1):
    for j in range(k):
        # 左端はi-区間右端
        lindex = i - r[j]
        rindex = i - l[j]
        dp[i] += dpsum[rindex] - dpsum[lindex - 1]
        dp[i] %= mod
    dpsum[i] = dpsum[i - 1] + dp[i]
    dpsum[i] %= mod
# print(dp)
# print(dpsum)

print((dp[n]))
