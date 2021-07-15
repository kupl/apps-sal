import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*a):
    return reduce(lcm_base, a, 1)

def lcm_list(a):
    return reduce(lcm_base, a, 1)

n = int(input())
a = list(map(int, input().split()))
mom = lcm_list(a)
a.sort()
num = []
for i in range(n):
    num.append(mom // a[i])
print(mom / sum(num))
