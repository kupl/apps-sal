
import time

n = int(input())
bm = {}
em = {}
bf = {}
ef = {}
a = []

for i in range(n):
    (s, b, e) = (i for i in input().split())
    b = int(b)
    e = int(e) + 1

    a.append(b)
    a.append(e)

    if s == 'M':
        if b in list(bm.keys()):
            bm[b] += 1
        else:
            bm[b] = 1

        if e in list(em.keys()):
            em[e] += 1
        else:
            em[e] = 1
    else:
        if b in list(bf.keys()):
            bf[b] += 1
        else:
            bf[b] = 1

        if e in list(ef.keys()):
            ef[e] += 1
        else:
            ef[e] = 1

start = time.time()

a = sorted(list(set(a)))

ans = 0
nf = 0
nm = 0

for i in a:
    if i in list(bm.keys()):
        nm += bm[i]
    if i in list(em.keys()):
        nm -= em[i]
    if i in list(bf.keys()):
        nf += bf[i]
    if i in list(ef.keys()):
        nf -= ef[i]

    t = min(nf, nm)

    if ans < 2 * t:
        ans = 2 * t

print(ans)
finish = time.time()
