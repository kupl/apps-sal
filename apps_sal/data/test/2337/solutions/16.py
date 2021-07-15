import sys
import math

n, m = [int(x) for x in (sys.stdin.readline()).split()]
an = [int(x) for x in (sys.stdin.readline()).split()]
bm = [int(x) for x in (sys.stdin.readline()).split()]

i = 0
j = 0
res = n
while(i < n):
    while(j < m and an[i] > bm[j]):
        j += 1  
        
    if(j < m and an[i] <= bm[j]):
        res -= 1
        j += 1
    
    i += 1
    
print(res)

