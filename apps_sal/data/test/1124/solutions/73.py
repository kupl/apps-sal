n = int(input())
l = list(map(int,input().split()))

import math
from functools import reduce

def gcd_list(numbers:list) -> int:
    return reduce(math.gcd, numbers)

print((gcd_list(l)))


