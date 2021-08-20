from math import *
(n, m) = input().split()
n = int(n)
m = int(m)
xcenters = [int(i) for i in input().split()]
result = []
for i in range(0, n):
    badones = []
    for j in range(0, i):
        if abs(xcenters[j] - xcenters[i]) <= 2 * m:
            badones.append(j)
    if len(badones) == 0:
        result.append(m)
        continue
    maxheight = m
    for x in badones:
        temp = result[x] + sqrt(4 * m * m - (xcenters[x] - xcenters[i]) ** 2)
        if maxheight < temp:
            maxheight = temp
    result.append(maxheight)
print(*result)
