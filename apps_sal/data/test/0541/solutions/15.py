from operator import itemgetter
(n, m) = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    (a[i], b[i]) = map(int, input().split())
ab = sorted([(a[i], b[i]) for i in range(m)], key=itemgetter(1))
removed = -1
ans = 0
for (a, b) in ab:
    if a > removed:
        removed = b - 1
        ans += 1
print(ans)
