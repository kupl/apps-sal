import sys
import math

n, r, avg = [int(x) for x in (sys.stdin.readline()).split()]
res = 0
k = []
vsum = 0
for i in range(n):
    a, b = [int(x) for x in (sys.stdin.readline()).split()]
    if(a >= r):
        vsum += r
    else:
        vsum += a
        k.append((r - a, b))
        
k.sort(key = lambda x: x[1])

val = n * avg - vsum
if(val <= 0):
    print(0)
    return

z = 0
i = 0
while(z < val):
    z += k[i][0]
    res += k[i][1] * k[i][0]
    i += 1
    
i -= 1
if(z > val):
    res -= (z - val) * k[i][1]
    print(res)
else:
    print(res)
        


    

