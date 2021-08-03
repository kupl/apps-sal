import math
from functools import reduce

n, m = map(int, input().split())
A = list(map(int, input().split()))


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(target_list):
    return reduce(lcm_base, target_list)


A_gcd = reduce(math.gcd, A)
flg = True

for a in A:
    if a // A_gcd % 2 == 0:
        flg = False
        break

if flg:
    min_x = int(lcm(A)) // 2
    ans = m // min_x - m // (2 * min_x)
    print(ans)
else:
    print(0)
