from bisect import bisect_left


def f():
    return map(int, input().split())


(n, x) = f()
(s, t) = ({}, {})
for i in range(n):
    (l, r, c) = f()
    d = r - l
    if d not in s:
        s[d] = []
    s[d].append((l, c))
for (d, p) in s.items():
    p.sort(key=lambda q: q[0])
    q = t[d] = [[l, c] for (l, c) in p]
    for i in range(1, len(q))[::-1]:
        q[i - 1][1] = min(q[i - 1][1], q[i][1])
m = 3000000000.0
for d in s:
    p = t.get(x - 2 - d, [])
    if p:
        for (l, c) in s[d]:
            i = bisect_left(p, [l + d + 1, 0])
            if i < len(p):
                m = min(m, c + p[i][1])
print(-1 if m == 3000000000.0 else m)
