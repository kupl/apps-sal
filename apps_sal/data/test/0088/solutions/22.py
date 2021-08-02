import itertools
import math
import bisect

one_zero = []
for i in range(2, 180):
    for k in range(1, i):
        one_zero.append(int('1' * k + '0' + '1' * (i - k - 1), base=2))


a, b = [int(x) for x in input().split()]
print(bisect.bisect_right(one_zero, b) - bisect.bisect_left(one_zero, a))
