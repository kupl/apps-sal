import itertools
import math
from collections import defaultdict


def input_ints():
    return list(map(int, input().split()))


def solve():
    x = int(input(), 2)
    ans = 0
    p = 1
    while p < x:
        ans += 1
        p *= 4
    print(ans)


def __starting_point():
    solve()


__starting_point()
