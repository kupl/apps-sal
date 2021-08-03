import math
n, d = [int(num) for num in input().split()]
c = 0
for i in range(n):
    x, y = [int(num) for num in input().split()]
    if math.sqrt(x**2 + y**2) <= d:
        c = c + 1
print(c)
