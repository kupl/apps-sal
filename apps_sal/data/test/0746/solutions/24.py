from math import *

a, b = list(map(int, input().split()))
n = int(input())

l = list()

for i in range(n):
    x, y, v = list(map(int, input().split()))
    t = sqrt((x - a)**2 + (y - b) ** 2) / v
    l.append(t)
print(min(l))
