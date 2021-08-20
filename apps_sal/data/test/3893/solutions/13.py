(x1, y1) = (int(x) for x in input().split())
(x2, y2) = (int(x) for x in input().split())
n = int(input())
ans = 0
for i in range(n):
    (a, b, c) = (int(x) for x in input().split())
    point1 = a * x1 + b * y1 + c
    point2 = a * x2 + b * y2 + c
    if point1 * point2 < 0:
        ans += 1
print(ans)
