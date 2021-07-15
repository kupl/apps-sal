import sys
import math

n = int(sys.stdin.readline())
an = [int(x) for x in (sys.stdin.readline()).split()]
m = int(sys.stdin.readline())

for i in range(m):
    x, y = [int(x) for x in (sys.stdin.readline()).split()]
    x -= 1
    if(x - 1 >= 0):
        an[x - 1] += y - 1
    if(x + 1 < n):
        an[x + 1] += an[x] - y
        
    an[x] = 0
    
for i in an:
    print(i)
    


