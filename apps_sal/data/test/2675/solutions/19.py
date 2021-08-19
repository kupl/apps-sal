from collections import Counter
(n, m) = map(int, input().split())
(p1, p2) = ([], [])
for i in range(n):
    (x, u) = map(int, input().split())
    p1.append(x * u)
for i in range(m):
    (y, v) = map(int, input().split())
    p2.append(y * v)
d1 = dict(Counter(p1))
d2 = dict(Counter(p2))
s = 0
for x in d1:
    if x in d2:
        s += min(d1[x], d2[x])
print(s)
