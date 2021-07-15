n=int(input())

import math
import sys

if n%2==0:
    print(n//2)
    return



xn=math.ceil(math.sqrt(n))
for i in range(2,xn+2):
    if n%i==0:
        print((n-i)//2+1)
        return
        

print(1)

