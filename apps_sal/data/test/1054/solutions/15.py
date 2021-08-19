def shag(x, y, xmin, ymin):
    (a, b) = list(map(int, input().split()))
    x = max(a, x)
    y = max(b, y)
    xmin = min(a, xmin)
    ymin = min(b, ymin)
    return (x, y, xmin, ymin)


k = int(input())
(x, y) = list(map(int, input().split()))
xmin = x
ymin = y
for i in range(1, k, 1):
    (x, y, xmin, ymin) = shag(x, y, xmin, ymin)
print(pow(max(x - xmin, y - ymin), 2))
