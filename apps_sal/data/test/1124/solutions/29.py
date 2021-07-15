import math
from functools import reduce
N=int(input())
a=list(map(int, input().split()))
b=[0]*N

mina=min(a)

#print(mina,a)

for i in range(N):
    if a[i]!=mina:
        b[i]=a[i]%mina+mina
    else:
        b[i]=mina
#print(b)

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

print(gcd(*b))
