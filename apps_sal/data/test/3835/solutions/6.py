from math import *
n = int(input())
v = [[int(g) for g in input().split()] for i in range(n)]
n1 = int(sqrt(v[0][1] * v[0][2] / v[1][2]))
print(n1, end=' ')
for i in range(1, n):
    print(v[0][i] // n1, end=' ')
