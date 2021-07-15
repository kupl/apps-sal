def solve():
    mod = 10**9+7
    n, k = list(map(int, input().split()))
    m = min(n-1,k)
    ans = 1
    dp0 = [1]*(m+1)
    dp1 = [1]*(m+1)
    for i in range(1,m+1):
        dp0[i] = dp0[i-1]*(n-i+1)*pow(i,mod-2,mod)%mod
        dp1[i] = dp1[i-1]*(n-i)*pow(i,mod-2,mod)%mod
        ans += dp0[i]*dp1[i]%mod
        ans %= mod
    return ans
print((solve()))

