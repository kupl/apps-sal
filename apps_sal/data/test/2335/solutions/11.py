r = g = b = 0
R = G = B = 0
s = u = v = 0
def f(k): return k if k else n


for i in range(int(input())):
    q, c = input().split()
    n = int(q)
    if c in 'RG':
        r, R, u = f(r), n, max(u, n - R)
    if c in 'BG':
        b, B, v = f(b), n, max(v, n - B)
    if c == 'G':
        if g:
            s -= max(u + v, n - G)
        g, G, u, v = f(g), n, 0, 0
print(s + R - r + G - g + B - b)
