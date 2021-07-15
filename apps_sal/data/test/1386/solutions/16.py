h, w = map(int,input().split())
mod = 998244353
ans = pow(2, h + w, mod)
print(ans%mod)
