pt = lambda *a, **k: print(*a, **k, flush=True)


def rd():
    return map(int, input().split())


(n, m) = rd()
an = list(rd())
bn = list(rd())
a1 = max(an)
a2 = min(an)
b1 = max(bn)
b2 = min(bn)
c1 = max(a1 * b1, a1 * b2)
c2 = max(a2 * b1, a2 * b2)
if c1 > c2:
    an.remove(a1)
else:
    an.remove(a2)
r = -4557430888798830399
for i in an:
    for j in bn:
        if i * j > r:
            r = i * j
pt(r)
