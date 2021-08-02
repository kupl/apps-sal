def f(): return map(int, input().split())
def g(x, y): return d.setdefault(x, set()).add(y)
def h(b): return a == b or b in d[a] or len(d[a] & d[b]) * 100 < k * len(d[a])


d = {}
m, k = f()
for i in range(m):
    a, b = f()
    g(a, b)
    g(b, a)
t = sorted(d)
for a in t:
    s = [str(b) for b in t if not h(b)]
    print(str(a) + ':', len(s), ' '.join(s))
