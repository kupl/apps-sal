import math
(n, d) = map(int, input().split())
count = 0
for i in range(n):
    (x, y) = map(int, input().split())
    a = math.sqrt(x * x + y * y)
    if a <= d:
        count += 1
print(count)
