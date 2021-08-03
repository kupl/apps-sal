m, k = map(int, input().split())
d = {}
for _ in range(m):
    x, y = map(int, input().split())
    d.setdefault(x, set()).add(y)
    d.setdefault(y, set()).add(x)
for x in sorted(d):
    ans = []
    for y in sorted(d):
        if y in d[x] or y == x:
            continue
        if len(d[x] & d[y]) * 100 >= k * len(d[x]):
            ans += [str(y)]
    print(str(x) + ':', len(ans), ' '.join(ans))
