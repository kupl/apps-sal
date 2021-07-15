import math
from functools import reduce

# 最小公倍数
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(l):
    """
    :param l: 最小公倍数を求めたいリスト
    :return: 最小公倍数
    """
    return reduce(lcm_base, l)

N = int(input())

l = [i for i in range(2,N+1)]
lcm_num = lcm(l)
print(lcm_num+1)
