(N, K, *l) = map(int, open((c := 0)).read().split())
d = {}
for (a, b) in zip(l[0::2], l[1::2]):
    d[a] = d.get(a, 0) + b
for k in sorted(d.keys()):
    if (c := (c + d[k])) >= K:
        break
print(k)
