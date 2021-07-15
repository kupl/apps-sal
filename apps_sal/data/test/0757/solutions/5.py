import sys
import math

n, m, k = [int(x) for x in (sys.stdin.readline()).split()]
an = [int(x) for x in (sys.stdin.readline()).split()]

an.sort(reverse = True)

res = 0
i = 0
while(m > k):
    if(i < n):
        k -= 1
        k += an[i]
        i += 1
    else:
        break
    
    res += 1

if(m <= k):    
    print(res)
else:
    print(-1)

