(n, m), *q = [[*list(map(int, i.split()))] for i in open(0)]
s = sorted(q)
d = {}
for k, v in s:
    if k not in d:
        d[k] = []
    d[k].append(v)
c = {}
for k, v in list(d.items()):
    i = 0
    if k not in c:
        c[k] = {}
    while i < len(v):
        i += 1
        c[k][v[~-i]] = str(i)
for p, y in q:
    pn = "00000" + str(p)
    cn = "00000" + c[p][y]
    print((pn[-6:] + cn[-6:]))
