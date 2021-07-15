from collections import defaultdict
from sys import stdin

input = stdin.readline

def solve():

    n = int(input())
    left = 1
    right = n + 1
    def ok(x):
        return x * (x - 1) <= 2 * (n + 1)
    while left < right:
        mid = left + right + 1 >> 1
        if ok(mid):
            left = mid
        else:
            right = mid - 1
    print(n - left + 2)


def __starting_point():
    solve()
__starting_point()
