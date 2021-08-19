from itertools import islice, cycle
import sys
from math import tan, pi, cos, sin
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__


def go():
    n = int(input())
    nn = 2 * n
    pin = pi / nn
    (l, r) = (0, pin)
    for i in range(100):
        c = (l + r) / 2
        if cos(c) - cos(pin - c) > 0:
            l = c
        else:
            r = c
    return cos(c) / sin(pin)


t = int(input())
ans = []
for _ in range(t):
    ans.append(str(go()))
print('\n'.join(ans))
