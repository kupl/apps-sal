import sys
import math

n = int(sys.stdin.readline())

id = [int(x) for x in (sys.stdin.readline()).split() if x != '0']

if(len(id) == 0):
    print(0)
    return

res = 0
id.sort()

v = id[0]
k = 1
for x in id[1:]:
    if(x == v):
        k += 1
    else:
        if(k == 2):
            res += 1
        elif(k > 2):
            print(-1)
            return
        v = x
        k = 1

if(k == 2):
    res += 1
elif(k > 2):
    print(-1)
    return  
    
print(res)      

