import sys
import math
import queue
MOD = 10**9 + 7
sys.setrecursionlimit(1000000)

n = int(input())
a = list(map(int, input().split()))
x = {}
for i in range(n):
    p = 0
    t = a[i]
    while t % 2 == 0:
        p += 1
        t = t >> 1
    if p in x:
        x[p].append(a[i])
    else:
        x[p] = [a[i]]
keep = []
for k in x:
    if len(x[k]) > len(keep):
        keep = x[k]
print(n - len(keep))
keep = set(keep)
for ai in a:
    if ai not in keep:
        print(ai, end=' ')
print()
