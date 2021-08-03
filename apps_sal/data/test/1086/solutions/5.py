def fold(x, m):
    y = 0
    for _ in range(m):
        y |= x & 1
        y <<= 1
        x >>= 1
    return x | y


def lmi(): return list(map(int, input().split()))


h, w = lmi()
a = [lmi() for _ in range(2 * h)]
g = [[abs(a[i][j] - a[i + h][j]) for j in range(w)] for i in range(h)]
m = 12801
mask = (1 << m) - 1

a = [0] * (w + 1)
a[0] = 1
for i in range(h):
    for j in range(w):
        cur, par = g[i][j], a[j] | a[j - 1]
        a[j] = par << cur & mask | fold(par, cur)
v = a[-2]
print((v & -v).bit_length() - 1)
