def gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    (d, x_, y_) = gcd(b, a % b)
    return (d, y_, x_ - a // b * y_)


def co(a, i):
    return f[a] * g[i] % 998244353 * g[a - i] % 998244353


(a, b, c) = map(int, input().split())
r = 0
f = [1]
g = []
for i in range(1, 5005):
    f.append(f[-1] * i % 998244353)
g = [gcd(i, 998244353)[1] for i in f]
for i in range(min(a, b) + 1):
    r += co(a, i) * co(b, i) % 998244353 * f[i] % 998244353
h = 0
for i in range(min(a, c) + 1):
    h += co(a, i) * co(c, i) % 998244353 * f[i] % 998244353
v = 0
for i in range(min(c, b) + 1):
    v += co(c, i) * co(b, i) % 998244353 * f[i] % 998244353
print(r * h * v % 998244353)
