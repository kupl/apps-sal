#!/usr/bin/env python3
import sys

def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()

n, L, a = rint()

t = []
l = []
for i in range(n):
    tt, ll = rint()
    t.append(tt)
    l.append(ll)

b = []
s = 0
for i in range(n):
    b.append(t[i] - s)
    s = t[i]+l[i]
b.append(L-s)


ans = 0
for bb in b:
    ans += bb//a

print(ans)




