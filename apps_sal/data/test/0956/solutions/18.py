d = {}
m, k = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    d.setdefault(a, set()).add(b)
    d.setdefault(b, set()).add(a)
for x in sorted(d):
    s = []
    for y in sorted(d):
        if x == y or y in d[x]:
            continue
        if len(d[x] & d[y]) * 100 >= k * len(d[x]):
            s += [str(y)]
    print(str(x) + ':', len(s), ' '.join(s))
