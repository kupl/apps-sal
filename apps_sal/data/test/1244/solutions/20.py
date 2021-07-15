import sys
import math

n = int(sys.stdin.readline())
an = [int(x) for x in (sys.stdin.readline()).split()]

d = dict()

for i in an:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
vmax = 0
vsum = 0
for i in list(d.keys()):
    vsum += d[i]
    if(d[i] > vmax):
        vmax = d[i]
        
if(vsum - vmax >= vmax - 1):
    print("YES")
else:
    print("NO")
    

