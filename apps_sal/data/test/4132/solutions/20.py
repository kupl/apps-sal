import math
from functools import reduce
n=int(input())
a=list(map(int,input().split()))

def gcd(numbers):
    return reduce(math.gcd, numbers)

print(gcd(a))
