from math import *

zzz = int(input())
for zz in range(zzz):
    a, b, x, y = list(map(int, input().split()))
    print(max(x * b, (a - x - 1) * b, y * a, (b - y - 1) * a))
