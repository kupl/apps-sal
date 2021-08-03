from math import *
n = int(input())
L = [int(x) for x in input().split()]
Max = 0
for i in range(len(L)):
    t = 0
    for j in range(i, len(L)):
        t ^= L[j]
        Max = max(Max, t)
print(Max)
