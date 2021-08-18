import math
import fractions
from functools import reduce

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [t // 2 for t in a]


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def num_dev2(x):
    return format(x, 'b')[::-1].find('1')


lcm = lcm_list(a)
q = m // lcm

count = 0
dev2 = num_dev2(a[0])
for i in range(1, n):
    if dev2 != num_dev2(a[i]):
        count += 1
        break
if count != 0:
    print(0)
else:
    print(math.ceil(q / 2))
