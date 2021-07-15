from math import *

for zz in range(int(input())):
    t = [int(i) for i in input()]
    n = len(t)
    if sum(t) == 0:
        print(*[0] * n, sep='')
    elif sum(t) == n:
        print(*[1] * n, sep='')
    else:
        print(*[0, 1] * (n), sep='')

