def da_generate(h, w, a):
    da = [[0] * w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1, w):
        da[0][i] = da[0][i - 1] + a[0][i]
    for i in range(1, h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i - 1][j] + cnt_w
    return da


def da_calc(da, p, q, x, y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y] - da[x][q - 1]
    if q == 0:
        return da[x][y] - da[p - 1][y]
    return da[x][y] - da[p - 1][y] - da[x][q - 1] + da[p - 1][q - 1]


(n, k) = map(int, input().split())
mototen = []
atuten = []
zax = []
zay = []
for i in range(n):
    (x, y) = map(int, input().split())
    mototen.append((x, y))
    zax.append(x)
    zay.append(y)
zax.sort()
zay.sort()
a = [[0 for i in range(len(zay))] for j in range(len(zax))]
for (x, y) in mototen:
    atx = zax.index(x)
    aty = zay.index(y)
    a[atx][aty] += 1
b = da_generate(len(zax), len(zay), a)
ans = float('inf')
for p in range(len(zax) - 1):
    for q in range(len(zay) - 1):
        for x in range(p + 1, len(zax)):
            for y in range(q + 1, len(zax)):
                kar = da_calc(b, p, q, x, y)
                if kar >= k:
                    men = (zax[x] - zax[p]) * (zay[y] - zay[q])
                    ans = min(ans, men)
print(ans)
