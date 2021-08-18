from fractions import Fraction
from math import ceil, floor

for _ in range(int(input())):
    h, c, t = list(map(int, input().split()))
    if t * 2 <= h + c:
        print(2)
    else:
        c1 = t - Fraction(h + c, 2)
        c2 = Fraction(h - c, 2)
        goal = c2 / c1
        goal1 = (goal + 1) / 2
        ans1 = floor(goal1) * 2 - 1
        ans2 = ceil(goal1) * 2 - 1
        if c2 / ans1 + c2 / ans2 <= c1 * 2:
            print(ans1)
        else:
            print(ans2)
