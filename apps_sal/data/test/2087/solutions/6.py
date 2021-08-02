mod1, mod2 = 10**9 + 7, 998244353
mod = mod2
def f(a): return int(a) * (int(a) + 1) % mod


a, b, c = map(f, input().split())
d = a * b * c % mod
print(d * pow(8, -1, mod) % mod)
