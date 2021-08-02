import sys
import math

an = []


def binary_s(st, key, z, ll):
    l = st
    r = ll
    while(l < r - 1):
        m = (l + r) // 2
        if(an[m] - z <= key):
            l = m
        else:
            r = m

    return r - st;


n, t = list(map(int, input().split()))

s = 0
for i in input().split():
    intt = int(i)
    an.append(s + intt)
    s += intt

res = 0
z = 0
for i in range(n):
    p = binary_s(i, t, z, n);

    if(p > res and an[i + p - 1] - z <= t):
        res = p

    z = an[i]
print(res)
