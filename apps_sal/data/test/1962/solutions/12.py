#!/usr/bin/env python3
from sys import stdin, stdout
from bisect import bisect

def rint():
    return map(int, stdin.readline().split())
#lines = stdin.readlines()

n, k, l = rint()

m = list(rint())

m.sort()
#print(m)
if m[-1] - m[0] > l:
    totcand = bisect(m, m[0]+l)
    #print(totcand)
    tot = 0
    i = 0
    nn = n
    while True:
        if nn == 0:
            break
        tot += m[i]
        i += 1
        nn -= 1
        totcand -= 1
        if totcand - (k-1)  >=  nn:
            i += (k-1)
            totcand -= (k-1)
        else:
            if totcand > nn:
                minus = totcand - nn
                i += minus
                totcand -= minus
            elif totcand < nn:
                print(0)
                return
    print(tot)
else:
    tot = 0
    for i in range(n):
        tot += m[i*k]

    print(tot)
