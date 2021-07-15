n,a,b = map(int,input().split())
mod = 10**9 + 7
ans = pow(2,n,mod) - 1
fa = 1
fb = 1
for i in range(1, a+1):
    fa *= i
    fa %= mod
for i in range(1, b+1):
    fb *= i
    fb %= mod

fa = pow(fa, mod-2, mod)
fb = pow(fb, mod-2, mod)

for i in range(a):
    fa *= n - i
    fa %= mod
for i in range(b):
    fb *= n - i
    fb %= mod

print((ans - fa - fb) % mod)
