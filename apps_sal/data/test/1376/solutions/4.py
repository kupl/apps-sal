n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(1, n + 1):
    d[i] = []
for i in range(2 * n):
    d[a[i]].append(i)
p1 = p2 = 0
ans = 0
for i in range(1, n + 1):
    (d1, d2) = (d[i][0], d[i][1])
    ans += min([abs(d1 - p1) + abs(d2 - p2), abs(d2 - p1) + abs(d1 - p2)])
    (p1, p2) = (d1, d2)
print(ans)
