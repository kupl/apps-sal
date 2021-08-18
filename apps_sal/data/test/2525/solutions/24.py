import collections
import math
import sys


def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]


mod = pow(10, 9) + 7


s = input()
n = N()
f = False
h = ''
t = ''
for i in range(n):
    q = input().split()
    if (len(q) == 1):
        f = not(f)
    else:
        if (f and q[1] == '1') or (not(f) and q[1] == '2'):
            t += q[2]
        else:
            h += q[2]
if f:
    ans = t[::-1] + s[::-1] + h
else:
    ans = h[::-1] + s + t
print(ans)
