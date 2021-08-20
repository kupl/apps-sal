import math
(n, d) = input().split()
n = int(n)
d = int(d)
count = 0
for i in range(n):
    (x, y) = input().split()
    x = int(x)
    y = int(y)
    rout = math.sqrt(x ** 2 + y ** 2)
    if rout <= d:
        count += 1
print(count)
