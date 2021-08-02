# import time
# start_time = int(round(time.time() * 1000))

from math import gcd


def solve(la, ra, ta, lb, rb, tb):

    m = gcd(ta, tb)
    m1 = la % m
    k = (lb - m1 + m - 1) // m
    y = k * m + m1

    return max(0, min(ra - la + 1, rb - y + 1))


la, ra, ta = list(map(int, input().split()))
lb, rb, tb = list(map(int, input().split()))


# print(solve(la, ra, ta, lb, rb, tb))
# print(solve(lb, rb, tb, la, ra, ta))

print(max(solve(la, ra, ta, lb, rb, tb), solve(lb, rb, tb, la, ra, ta)))


# end_time = int(round(time.time() * 1000))
# print('Execution Time : ', (end_time - start_time), 'ms')
