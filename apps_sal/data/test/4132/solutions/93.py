N=int(input())
A=map(int,input().split())
import math
from functools import reduce

print(reduce(math.gcd, A))
