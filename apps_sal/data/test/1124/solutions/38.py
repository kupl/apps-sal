from math import gcd
from functools import reduce
input()
a=list(map(int,input().split()))
sum=reduce(lambda x,y:gcd(x,y),a)
print(sum)
