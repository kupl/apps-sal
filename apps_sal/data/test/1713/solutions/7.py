import sys
import math

n, s, t = [int(x) for x in (sys.stdin.readline()).split()]
p = [int(x) for x in (sys.stdin.readline()).split()]

res = 0
k = s
while(s != t):
    s = p[s - 1]
    res += 1
    if(k == s):
        print(-1)
        return
    
print(res)
