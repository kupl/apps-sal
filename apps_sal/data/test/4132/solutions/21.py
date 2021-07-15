n = int(input())
L = list(map(int,input().split()))

from math import gcd
from functools import reduce

ans = reduce(gcd,L)
print(ans)
