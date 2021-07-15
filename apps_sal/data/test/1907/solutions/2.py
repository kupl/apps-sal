from collections import namedtuple
from math import hypot, pi


def contains(fst, scd):
    return hypot(fst.x - scd.x, fst.y - scd.y) < fst.r


def area(circle):
    return pi * circle.r ** 2


def find_prev(side, circle):
    for prev in reversed(side):
        if contains(prev, circle):
            return prev


Circle = namedtuple('Circle', 'x y r')

n = int(input())
cs = []
for i in range(n):
    cs.append(Circle(*list(map(int, input().split()))))

cs = sorted(cs, key=lambda circle: -circle.r)
ans = 0.0
counts = dict()
left = []
right = []
for ind, cur in enumerate(cs):
    prev_left = find_prev(left, cur)
    prev_right = find_prev(right, cur)
    if prev_left is None:
        left.append(cur)
        counts[cur] = True
        ans += area(cur)
    elif prev_right is None:
        right.append(cur)
        counts[cur] = True
        ans += area(cur)
    elif counts[prev_left]:
        left.append(cur)
        counts[cur] = False
        ans -= area(cur)
    else:
        left.append(cur)
        counts[cur] = True
        ans += area(cur)

print(ans)

