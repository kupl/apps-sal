__author__ = 'Rakshak.R.Hegde'
(n, r, avg) = map(int, input().split())
ab = []
d = n * avg
for i in range(n):
    (a, b) = map(int, input().split())
    d -= a
    ab.append((b, a))
ab.sort()
cost = 0
for t in ab:
    if d <= 0:
        break
    if t[1] < r:
        m = min(d, r - t[1])
        cost += m * t[0]
        d -= m
print(cost)
