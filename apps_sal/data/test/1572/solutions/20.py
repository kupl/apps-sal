import sys
import math

n = int(sys.stdin.readline())
an = [int(x) for x in (sys.stdin.readline()).split()]

if(n == 1 or n == 2):
    print(n)
    return

vmax = 2

r = vmax
for i in range(2, n):
    if(an[i] == (an[i - 1] + an[i - 2])):
        r += 1
    else:
        if(r > vmax):
            vmax = r
        r = 2

if(r > vmax):
    vmax = r

print(vmax)
