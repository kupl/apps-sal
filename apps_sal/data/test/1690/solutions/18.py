from functools import reduce
from collections import Counter
import sys
sys.setrecursionlimit(2000)


def __starting_point():
    n = [int(val) for val in sys.stdin.readline().split()][0]
    a = [int(val) for val in sys.stdin.readline().split()]
    prev = a[-1]
    count = prev
    for i in range(n - 2, -1, -1):
        prev = min(a[i], prev - 1)
        prev = max(prev, 0)
        count += prev
    print(count)


__starting_point()
