import math
from functools import reduce


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


N = int(input())
N_List = []
for i in range(N):
    N_List.append(int(input()))
print(lcm_list(N_List))
