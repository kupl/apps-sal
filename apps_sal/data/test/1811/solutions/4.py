import sys
import math

n, k = [int(x) for x in (sys.stdin.readline()).split()]
an = sys.stdin.readline()

z = 0
for i in range(n):
    if(an[i] == '.'):
        if(i + 1 - z <= k):
            z = i + 1

if(n + 1 - z <= k):
    print("YES")
else:
    print("NO")            



        

    

