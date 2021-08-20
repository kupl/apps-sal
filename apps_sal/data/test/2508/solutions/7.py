(h, a, *m) = open(0)
(h, w, k, a, b, f, g) = map(int, (h + a).split())
d = [(I := (h * w))] * I
m += (d,)
q = [(a := (~w + a * w + b))]
d[a] = 1
for s in q:
    for (y, x) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        for z in range(k):
            if '.' != m[(i := (s // w + y * ~z))][(j := (s % w + x * ~z))] or (p := (d[s] + 1)) > d[(t := (i * w + j))]:
                break
            if d[t] > p:
                q += (t,)
                d[t] = p
print(d[~w + f * w + g] % I - 1)
