u, v, d = {}, {}, set()
for i in range(int(input())):
    t = input()
    if len(t) == 1: d.add(t)
    for a, b in zip(t, t[1:]):
        if u.get(a, b) != b or v.get(b, a) != a: print('NO');return
        u[a], v[b] = b, a
d = d - set(u) - set(v)
for q in set(u).difference(v):
    while q[-1] in u: q += u.pop(q[-1])
    d.add(q)
if u: print('NO');return
print(''.join(sorted(d)))
