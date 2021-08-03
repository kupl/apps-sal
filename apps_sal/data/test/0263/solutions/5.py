import math
n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(int(input()))
maxs = max(a)
m1 = m
for i in a:
    m -= (maxs - i)

print(maxs + max(math.ceil(m / n), 0), maxs + m1)
