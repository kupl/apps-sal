H, W, A, B = map(int, input().split())
mod = int(1e9) + 7


def inved(a):
    x, y, u, v, k, l = 1, 0, 0, 1, a, mod
    while l != 0:
        x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
        k, l = l, k % l
    return x % mod


fact = [1 for _ in range(H + W + A + B + 1)]
invf = [1 for _ in range(H + W + A + B + 1)]
for i in range(H + W + A + B):
    fact[i + 1] = (fact[i] * (i + 1)) % mod
invf[-1] = inved(fact[-1])
for i in range(H + W + A + B, 0, -1):
    invf[i - 1] = (invf[i] * i) % mod
S = 0
for i in range(H - A):
    S += (fact[i + B - 1] * invf[i] * fact[H - i + W - B - 2] * invf[H - 1 - i]) % mod
    S %= mod
S *= (invf[B - 1] * invf[W - B - 1]) % mod
S %= mod

print(S)
