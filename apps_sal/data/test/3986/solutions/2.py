import sys
import math
  
n, k = [int(x) for x in (sys.stdin.readline()).split()]

if(k == 1 and n == 1):
    print("a")
    return

if(k == 1 or k > n):
    print(-1)
    return

res = []
t = 2
for i in range(n):
    if(n - (k - 2) > i):
        if(i % 2 == 0):
            res.append('a')
        else:
            res.append('b')
    else:
        res.append(chr(t + 97))
        t += 1
        
print("".join(res))
