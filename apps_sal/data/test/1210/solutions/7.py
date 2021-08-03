import math
from fractions import Fraction

n, p = [int(x) for x in input().split()]
exp_mean = 0
first_l, first_r = None, None
last_good, last_all = None, None

for i in range(n + 1):
    l, r = None, None
    if i < n:
        l, r = [int(x) for x in input().split()]
        if first_l is None:
            first_l, first_r = l, r
    else:
        l, r = first_l, first_r

    upper = r // p
    lower = math.ceil(l / p)

    cur_good = upper - lower + 1
    cur_all = r - l + 1

    if last_good is not None:
        cur_mean = float(2000 * (cur_good * last_good + (cur_all - cur_good) *
                         last_good + (last_all - last_good) * cur_good) / (
                         cur_all * last_all))
        exp_mean += cur_mean

    last_good = cur_good
    last_all = cur_all

print(exp_mean)
