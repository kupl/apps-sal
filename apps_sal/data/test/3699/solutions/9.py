from math import sqrt

ax, ay, bx, by, tx, ty = list(map(int, input().split()))
n = int(input())
d = 0
mina = (2 * 10**9, 0, 0)
mina2 = (2 * 10**9, 0, 0)
minb = (2 * 10**9, 0, 0)
minb2 = (2 * 10**9, 0, 0)
for _ in range(n):
    x, y = list(map(int, input().split()))
    dt = sqrt((x - tx)**2 + (y - ty)**2)
    d += 2 * dt
    da = sqrt((ax - x)**2 + (ay - y)**2)
    dat = (da - dt, x, y)
    if dat[0] < mina[0]:
        mina, mina2 = dat, mina
    elif dat[0] < mina2[0]:
        mina2 = dat
    db = sqrt((bx - x)**2 + (by - y)**2)
    dbt = (db - dt, x, y)
    if dbt[0] < minb[0]:
        minb, minb2 = dbt, minb
    elif dbt[0] < minb2[0]:
        minb2 = dbt
if n >= 2 and mina[0] < 0 and minb[0] < 0:
    if mina[1] != minb[1] or mina[2] != minb[2]:
        d += mina[0] + minb[0]
    elif mina2[0] < 0 and minb2[0] < 0:
        d += min(mina[0] + minb2[0], mina2[0] + minb[0])
    elif mina2[0] < 0:
        d += min(mina[0], mina2[0] + minb[0])
    elif minb2[0] < 0:
        d += min(mina[0] + minb2[0], minb[0])
    else:
        d += min(mina[0], minb[0])
else:
    d += min(mina[0], minb[0])
print(d)
