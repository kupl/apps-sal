[n, a, b] = list(map(int, input().strip().split()))
bis = [tuple(map(int, input().strip().split())) for _ in range(n)]
dis = [(a * Vx - Vy, Vx) for (x, Vx, Vy) in bis]
dis.sort()
res = 0
dprev = dis[0][0] - 1
vprev = 0
dcount = 0
vcount = 0
for (di, vi) in dis:
    if di != dprev:
        res += dcount * (dcount - 1)
        res -= vcount * (vcount - 1)
        dcount = 1
        vcount = 1
        dprev = di
        vprev = vi
    else:
        dcount += 1
        if vi != vprev:
            res -= vcount * (vcount - 1)
            vcount = 1
            vprev = vi
        else:
            vcount += 1
res += dcount * (dcount - 1)
res -= vcount * (vcount - 1)
print(res)
