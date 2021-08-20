MOD = 998244353
(a, b, c) = map(int, input().split())


def f(x):
    return x * (x + 1) // 2 % MOD


(x, y, z) = (f(a), f(b), f(c))
print(f(a) * f(b) * f(c) % MOD)
