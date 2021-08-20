import math
from functools import reduce
(n, m) = input().split()
a = list(map(int, input().split()))
b = [0] * int(n)
for i in range(len(a)):
    b[i] = a[i] // 2


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


c = 0
x = lcm_list(b)
for i in range(int(n)):
    if x // b[i] % 2 == 0:
        c = -1
        break
    else:
        continue
if c == -1:
    print(0)
else:
    print(math.floor((int(m) / x + 1) / 2))
