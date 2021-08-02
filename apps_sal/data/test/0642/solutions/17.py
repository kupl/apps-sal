

"""k = []
for i in range(5):
    k.append([int(x) for x in (sys.stdin.readline()).split()])
    
vmax = 0 
tt = []
for i in range(5):
    for j in range(i, 5):
        if(i != j):
            k[i][j] = k[j][i] = k[i][j] + k[j][i]
                

for i in range(5):
    print(k[i])"""


import sys
import math

n, m = [int(x) for x in (sys.stdin.readline()).split()]
dm = [int(x) for x in (sys.stdin.readline()).split()]

dm.sort()

if(m == 0):
    print("YES")
    return

if(dm[0] == 1 or dm[m - 1] == n):
    print("NO")
    return

val = 0
for i in range(m - 1):
    if(math.fabs(dm[i] - dm[i + 1]) == 1):
        val += 1
    else:
        val = 0
    if(val > 1):
        print("NO")
        return

print("YES")
