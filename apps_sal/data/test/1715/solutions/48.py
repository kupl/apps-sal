a, b, q = map(int, input().split())
tl = []
qlist = []
for i in range(a):
    tl.append((int(input()), 0, i))
for i in range(b):
    tl.append((int(input()), 1, i))
for i in range(q):
    q1 = int(input())
    tl.append((q1, 2, i))
    qlist.append(q1)
tl.sort()
prea = [-1] * q
preb = [-1] * q
ta = tb = -1
for i, c in enumerate(tl):
    if c[1] == 0:
        ta = c[0]
    elif c[1] == 1:
        tb = c[0]
    elif c[1] == 2:
        prea[c[2]], preb[c[2]] = ta, tb
posta = [-1] * q
postb = [-1] * q
ra = rb = -1
for i, c in enumerate(tl[::-1]):
    if c[1] == 0:
        ra = c[0]
    elif c[1] == 1:
        rb = c[0]
    elif c[1] == 2:
        posta[c[2]], postb[c[2]] = ra, rb


def cal(pra, poa, prb, pob, q):
    gmin = 999999999999
    if pra != -1 and prb != -1:
        if pra < prb:
            gmin = min(gmin, q - pra)
        else:
            gmin = min(gmin, q - prb)
    if pra != -1 and pob != -1:
        gmin = min(gmin, pob - pra + min(q - pra, pob - q))
    if prb != -1 and poa != -1:
        gmin = min(gmin, poa - prb + min(poa - q, q - prb))
    if poa != -1 and pob != -1:
        if poa < pob:
            gmin = min(gmin, pob - q)
        else:
            gmin = min(gmin, poa - q)
    return gmin


for a1, a2, b1, b2, q in zip(prea, posta, preb, postb, qlist):
    print(cal(a1, a2, b1, b2, q))
