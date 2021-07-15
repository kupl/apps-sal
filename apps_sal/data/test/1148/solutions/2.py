import itertools
import math

n = int(input())
a = [int(x) for x in input().split()]
amin = min(a)
b = list([x for x in enumerate(a) if x[1] == amin])
l = len(b)
k = max((b[(i+1) % l][0] - b[i][0] - 1)%n for i in range(l))
print(amin*n + k)



