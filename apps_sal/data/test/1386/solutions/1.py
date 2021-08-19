(w, h) = list(map(int, input().split()))


def powermod(x, y, mod):
    if y == 0:
        return 1
    return powermod(x * x % mod, y // 2, mod) * (x if y % 2 else 1) % mod


print(powermod(2, w + h, 998244353))
