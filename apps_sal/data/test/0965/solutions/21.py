from collections import defaultdict, deque, Counter, OrderedDict
from bisect import insort, bisect_right, bisect_left
import threading
import sys


def main():
    n = int(input())
    s = input()
    a = s.count('A')
    i = s.count('I')
    ans = 0
    if i == 0:
        ans = a
    elif i == 1:
        ans = 1
    print(ans)


def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)"""
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
