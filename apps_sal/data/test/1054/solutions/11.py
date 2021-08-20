n = int(input())
(x, y) = map(int, input().split())
xmin = x
xmax = x
ymin = y
ymax = y
for i in range(n - 1):
    (x, y) = map(int, input().split())
    xmin = min(xmin, x)
    xmax = max(xmax, x)
    ymin = min(ymin, y)
    ymax = max(ymax, y)
print(max(ymax - ymin, xmax - xmin) ** 2)
