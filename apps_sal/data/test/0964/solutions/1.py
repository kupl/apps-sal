w1, h1, w2, h2, w3, h3 = map(int, input().split())
r1, r2, r3 = sorted((w1, h1)), sorted((w2, h2)), sorted((w3, h3))
for i in range(3):
    ra, ca = (r1, r2, r3)[i], "ABC"[i]
    rb, cb = (r1, r2, r3)[(i + 1) % 3], "ABC"[(i + 1) % 3]
    rc, cc = (r1, r2, r3)[(i + 2) % 3], "ABC"[(i + 2) % 3]
    if ra[0] == ra[1]:
        continue
    # solve a ra[1]-ra[0] x ra[1] rectangle with 2 remaining rectangles
    w, h = ra[1] - ra[0], ra[1]
    rs = []
    wtot, whit, ws = 0, 0, []
    htot, hhit, hs = 0, 0, []
    for r in (rb, rc):
        rs.append(r)
        if r[0] != r[1]:
            rs.append((r[1], r[0]))
    for r in rs:
        if r[0] == w:
            wtot += r[1]
            whit += 1
            ws.append(r[1])
        if r[0] == h:
            htot += r[1]
            hhit += 1
            hs.append(r[1])
    if whit == 2 and wtot == h:
        n = ra[1]
        xb = rb[0] if rb[1] == w else rb[1]
        xc = rc[0] if rc[1] == w else rc[1]
        print(n)
        print((ca * n + '\n') * ra[0], end='')
        print((cb * xb + cc * xc + '\n') * w, end='')
        break
    if hhit == 2 and htot == w:
        n = ra[1]
        xb = rb[0] if rb[1] == h else rb[1]
        xc = rc[0] if rc[1] == h else rc[1]
        print(n)
        print((ca * n + '\n') * ra[0], end='')
        print((cb * n + '\n') * xb, end='')
        print((cc * n + '\n') * xc, end='')
        break
else:
    print(-1)
