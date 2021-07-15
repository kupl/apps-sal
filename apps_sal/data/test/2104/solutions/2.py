import sys
import math

l,r=map(int,input().strip().split())
print("YES")
comma=[int(x) for x in range(l,r+1)]
for a in range(0,len(comma)-1,2):
    print(comma[a],comma[a+1])
