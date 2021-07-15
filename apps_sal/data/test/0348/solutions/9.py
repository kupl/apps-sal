mod = 998244353
n,m,l,r = list(map(int,input().split()))

if (n * m) % 2 == 1:
    res = pow(r - l + 1, n * m, mod)
    print(res)
    return

def f(p):
    return p // 2

def g(p):
    return (p + 1) // 2

# 偶数
even = f(r) - f(l - 1)
odd = g(r) - g(l - 1)

res = (pow(even - odd, n * m, mod) + pow(even + odd, n * m, mod)) * pow(2, mod - 2, mod)
res %= mod
print(res)

