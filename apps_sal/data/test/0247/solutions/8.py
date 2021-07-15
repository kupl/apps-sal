from collections import Counter
from random import choice
from sys import stdin
from time import time

from math import gcd


def get_v(p0, p1):
    dp = (p1[0] - p0[0], p1[1] - p0[1])

    g = gcd(*dp)

    if dp[0] > 0:
        return (dp[0] // g, dp[1] // g)

    elif dp[0] < 0:
        return (-dp[0] // g, -dp[1] // g)

    else:
        return (dp[0] // g, abs(dp[1] // g))


all_in = stdin.read().splitlines()

n = int(all_in[0])
points = [tuple(map(int, el.split())) for el in all_in[1:]]

if n <= 4:
    print('YES')
    return

p_max_ = 1

t = time()
while p_max_ == 1:
    p = choice(points)

    v_s = [get_v(p, x) for x in points if x != p]

    if len(set(v_s)) <= 2:
        print('YES')
        return

    C = Counter(v_s)

    p_max, p_max_ = sorted(list(C.items()), key=lambda x: x[1])[-1]

    if time() - t > 1.75:
        print('NO')
        return

points.remove(p)
points_ = [points[i - 1] for i in range(1, n) if v_s[i - 1] != p_max]

if len(points_) <= 2:
    print('YES')
    return

p_ = choice(points_)

v_s_ = [get_v(p_, x) for x in points_ if x != p_]

if len(set(v_s_)) >= 2:
    print('NO')
    return

print('YES')

