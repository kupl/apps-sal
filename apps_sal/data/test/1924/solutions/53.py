u, l, d, r = map(int, input().split())
mod = 10 ** 9 + 7

def extGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extGCD(b, a%b)
    y -= a//b * x
    return g, x, y

def moddiv(a, b):
    _, inv, _ = extGCD(b, mod)
    return (a * inv) % mod

f = [0] * (2 * 10 ** 6 + 10)
f[0] = 1
for i in range(1, 2 * 10 ** 6 + 10):
    f[i] = (f[i-1] * i) % mod

def comb(a, b):
    return moddiv(moddiv(f[a+b], f[a]), f[b])

ans = 0
d += 1
r += 1
ans += comb(d, r)
ans += comb(u, l)
ans -= comb(d, l)
ans -= comb(u, r)
print(ans % mod)
