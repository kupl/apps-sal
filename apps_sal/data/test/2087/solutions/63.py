a, b, c = map(int, input().split())
mod = 998244353 
a = a*(a+1)//2 % mod if a != 1 else 1
b = b*(b+1)//2 % mod if b != 1 else 1
c = c*(c+1)//2 % mod if c != 1 else 1
print((a*b*c)%mod)
