(d1, d2, d3, d4) = (0, 0, 0, 0)
(e1, e2, e3, e4) = (0, 0, 0, 0)
(n, x) = map(int, input().split())
A = list(map(int, input().split())) + [0]
for a in A:
    e1 = max(a, d1 + a)
    e2 = max(x * a, d1 + x * a, d2 + x * a)
    e3 = max(e1, d2 + a, d3 + a)
    e4 = max(d1, d2, d3, d4, a)
    (d1, d2, d3, d4) = (e1, e2, e3, e4)
print(d4)
