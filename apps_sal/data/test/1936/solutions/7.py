import io
import os
import sys
from collections import deque, defaultdict


def _input():
    x = sys.stdin.readline()
    x = x.replace('\r', '')
    x = x.replace('\n', '')
    return x


if 'STDINPUT' not in os.environ:
    input = _input
else:
    print('Standard input')


def solve():
    (l, r) = [int(x) for x in input().split()]
    if l * 2 > r:
        print(-1, -1)
    else:
        print(l, l * 2)


test_cases = True
if test_cases:
    _q = int(input())
    for _ in range(_q):
        solve()
else:
    solve()
