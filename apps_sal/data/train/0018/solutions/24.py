from itertools import islice, cycle
import sys
from math import tan, pi
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__


def go():
    n = int(input())
    return 1 / tan(pi / (2 * n))


t = int(input())
ans = []
for _ in range(t):
    ans.append(str(go()))
print('\n'.join(ans))
