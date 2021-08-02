import math
n, d = map(int, input().split())
count = 0
for i in range(n):
    x, y = map(int, input().split())
    if math.sqrt(x**2 + y**2) <= d:
        count += 1
print(count)
