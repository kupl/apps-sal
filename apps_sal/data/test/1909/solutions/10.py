import sys
import math

n, k = [int(x) for x in (sys.stdin.readline()).split()]
an = [int(x) for x in (sys.stdin.readline()).split()]

vmin = 1000000000
rez = 0
for i in range(k):
    vsum = 0
    vvmin = 1001
    for j in range(i, n, k):
        vsum += an[j]

    if(vsum < vmin):
        vmin = vsum
        rez = i + 1

print(rez)
