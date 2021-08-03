from collections import defaultdict, deque, Counter, OrderedDict
from bisect import insort, bisect_right, bisect_left
import threading
import sys


def main():
    n, k = list(map(int, input().split()))
    ans = 0
    if n < k:
        ans = k
    else:
        ex = n % k
        ans = n + (k - n % k)
    print(ans)


def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)"""
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
