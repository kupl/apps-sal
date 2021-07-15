from sys import stdin
from math import sqrt

r, d = list(map(int, stdin.readline().split()))
n = int(stdin.readline())
data = []
for i in range(0, n):
    data.append(list(map(int, stdin.readline().split())))

rs = 0
for i in range(0, n):
    D = sqrt(data[i][0] ** 2 + data[i][1] ** 2)
    rs += 1 if (r - d <= D - data[i][2] and r >= D + data[i][2]) else 0

print(rs)

