import sys
import math

n = int(sys.stdin.readline())

k = dict()
for i in range(n):
    a, b = [int(x) for x in (sys.stdin.readline()).split()]
    if a in k:
        if(k[a][0] > b):
            k[a][0] = b
        if(k[a][1] < b):
            k[a][1] = b
    else:
        k[a] = [b] * 2

t = list(k.keys())
t.sort()

res = min(t[0], k[t[0]][1])

for i in t[1:]:
    if(k[i][0] >= res):
        res = min(k[i][1], i)
    else:
        res = i

print(res)
