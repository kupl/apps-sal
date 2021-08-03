from sys import stdin
from itertools import combinations
from math import ceil, fabs
input = stdin.readline
n = int(input())
#n, m = list(map(int, input().split()))
a = [float(input()) for _ in range(n)]
l = len(a)
m = []
d = []
for i in range(l):
    if a[i] == int(a[i]):
        d.append(int(a[i]))
        m.append(1)
    else:
        m.append(0)
        if a[i] < 0:
            d.append(int(a[i] - 1))
        else:
            d.append(int(a[i]))
s = sum(d)
if s == 0:
    for i in d:
        print(i)
elif s < 0:
    for i in range(l):
        if m[i] == 0:
            d[i] += 1
            s += 1
            if s == 0:
                for i in d:
                    print(i)
                break
