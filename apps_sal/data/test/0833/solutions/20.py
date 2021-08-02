n, v = map(int, input().split())
d, s = {}, 0
for i in range(n):
    a, b = map(int, input().split())
    d[a] = d.get(a, 0) + b
    s += b

r = v
for i in sorted(d.keys()):
    d[i] -= min(d[i], r)
    r, b = v, min(d[i], v)
    d[i] -= b
    if i + 1 in d:
        r -= b

print(s - sum(d.values()))
