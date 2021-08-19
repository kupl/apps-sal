import math
(r, d) = map(int, input().split())
n = int(input())
c = 0
for i in range(n):
    (x, y, z) = map(int, input().split())
    if math.sqrt(x ** 2 + y ** 2) - z >= r - d and math.sqrt(x ** 2 + y ** 2) + z <= r:
        c += 1
print(c)
