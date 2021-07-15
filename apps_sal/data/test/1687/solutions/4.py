import sys
import math

n = int(sys.stdin.readline())
an = [int(x) for x in (sys.stdin.readline()).split()]

vmin = 1000000001

for i in an:
    if(i < vmin):
        vmin = i

for i in an:
    if(i % vmin != 0):
        print(-1)
        return
    
print(vmin)  
