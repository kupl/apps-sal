n, m = list(map(int, input().split()))
mod = 10**9+7
k = (pow(2,m,mod)+mod-1)%mod
print((pow(k, n, mod)+mod)%mod)

