MOD = 998244353
a, b, c = map(int, input().split())
f = lambda x: x * (x + 1) // 2 % MOD
x, y, z = f(a), f(b), f(c)
print(f(a) * f(b) * f(c) % MOD)
