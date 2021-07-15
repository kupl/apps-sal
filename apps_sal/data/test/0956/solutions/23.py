f = lambda: map(int, input().split())
g = lambda x, y: d.setdefault(x, set()).add(y)
d = {}
m, k = f()
for i in range(m):
    a, b = f()
    g(a, b)
    g(b, a)
t = sorted(d)
for a in t:
    s = [str(b) for b in t if a != b and b not in d[a] and len(d[a] & d[b]) * 100 >= k * len(d[a])]
    print(str(a) + ':', len(s), ' '.join(s))
