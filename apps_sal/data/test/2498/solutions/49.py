from functools import reduce
import math


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a = [i // 2 for i in list(set(a))]
nothing = False
cnt_common = -1
for i in a:
    cnt = 0
    while i % 2 == 0:
        i = i // 2
        cnt += 1
    if cnt_common == -1:
        cnt_common = cnt
        continue
    if cnt_common != cnt:
        nothing = True
        break
b = lcm_list(a)
if nothing:
    print(0)
else:
    ans = (m - b) // (2 * b) + 1
    print(max(ans, 0))
