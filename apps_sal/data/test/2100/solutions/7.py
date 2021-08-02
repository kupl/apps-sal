import sys
import math

n = int(sys.stdin.readline())

lc = 0
rc = 0
lo = 0
ro = 0
for i in range(n):
    l, r = [int(x) for x in (sys.stdin.readline()).split()]
    if(l == 1):
        lc += 1
    else:
        lo += 1
    if(r == 1):
        rc += 1
    else:
        ro += 1

res = 0
if(rc >= ro):
    res += ro
else:
    res += rc

if(lc >= lo):
    res += lo
else:
    res += lc

print(res)
