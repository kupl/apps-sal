a, b, c = map(int, input().split())
mod = 998244353


def f(x):
    return (x * (x + 1) // 2) % mod


print(f(a) * f(b) * f(c) % mod)
