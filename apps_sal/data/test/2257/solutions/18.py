(n, a, b, x, y) = map(int, input().split())
li = [[0, 0]]
for _ in range(n):
    (p, q) = map(int, input().split())
    li.append([(a - p) ** 2 + (b - q) ** 2, (x - p) ** 2 + (y - q) ** 2])
li = sorted(li)
mn = 1000000000000000000000000
for i in range(n + 1):
    mx = 0
    for j in range(i + 1, n + 1):
        if li[j][0] > li[i][0]:
            mx = max(mx, li[j][1])
    mn = min(mn, mx + li[i][0])
print(mn)
