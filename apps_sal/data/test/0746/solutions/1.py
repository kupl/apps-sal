from math import hypot
(a, b) = map(int, input().split())
res = 1e+308
for i in range(int(input())):
    (x, y, v) = map(int, input().split())
    res = min(res, hypot(a - x, b - y) / v)
print(res)
