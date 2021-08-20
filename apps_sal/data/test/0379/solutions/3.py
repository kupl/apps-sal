(h, w) = map(int, input().split())
g = [input() for _ in range(h)]
mh = mw = 10000000
Mh = Mw = 0
for i in range(h):
    for j in range(w):
        if g[i][j] == 'X':
            mh = min(mh, i)
            Mh = max(Mh, i)
            mw = min(mw, j)
            Mw = max(Mw, j)
r = 'YES'
for i in range(h):
    for j in range(w):
        if (g[i][j] == 'X') != (mh <= i <= Mh and mw <= j <= Mw):
            r = 'NO'
print(r)
