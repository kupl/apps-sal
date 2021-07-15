n = int(input())
x, y = (int(x) for x in input().split())
x1, y1, x2, y2 = x, y, x, y
for i in range(n - 1):
    x, y = (int(x) for x in input().split())
    x1 = min(x1, x)
    x2 = max(x2, x)
    y1 = min(y1, y)
    y2 = max(y2, y)
print(max(x2 - x1, y2 - y1) ** 2)
