import sys
n, m, k, l = [int(s) for s in input().split()]
if (k + l) % m != 0:
    i = (k + l) // m + 1
else:
    i = (k + l) // m
if i * m > n:
    print(-1)
else:
    print(i)
