import sys
import math


n = int(sys.stdin.readline())

k = [0] * 1001
l = []
for i in range(n):
    a, b = [int(x) for x in (sys.stdin.readline()).split()]
    k[b] += 1
    
    l.append((a, b))
    
res = 0
for i in l:
    if(i[0] == i[1] and k[i[0]] == 1):
        res += 1
        
    if(k[i[0]] == 0):
        res += 1
        
print(res)

