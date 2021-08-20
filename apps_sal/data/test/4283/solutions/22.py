n = int(input())
a = [int(x) for x in input().split()]
a.sort()
(p1, p2) = (0, 0)
r = 1
while p2 < n - 1:
    p2 += 1
    while a[p2] - a[p1] > 5:
        p1 += 1
    r = max(r, p2 - p1 + 1)
print(r)
