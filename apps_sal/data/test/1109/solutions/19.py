
import sys
import math
  
n, k = [int(x) for x in (sys.stdin.readline()).split()]
an = [int(x) for x in (sys.stdin.readline()).split()]

res = 0
for i in range(k):
    k1 = 0
    k2 = 0
    for j in range(i, n, k):
        if(an[j] == 1):
            k1 += 1
        else:
            k2 += 1       
    res += int(n / k) - max(k2, k1)
    
print(res)
