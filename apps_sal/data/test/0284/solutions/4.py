from collections import defaultdict, deque, Counter, OrderedDict
from bisect import insort, bisect_right, bisect_left
import threading
import sys


def main():
    n = int(input())
    a = 1234567
    b = 123456
    c = 1234
    if n % 2 != 0:
        n -= a
        if n < 0:
            print("NO")
            return
    for i in range(0, 1000):
        now = a * i
        toc = n - now
        if toc < 0:
            print("NO")
            return
        j = 0
        while j * b <= toc:
            if (toc - j * b) % c == 0:
                print("YES")
                return
            j += 1


def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)"""
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
