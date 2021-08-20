from functools import reduce
from collections import Counter
import sys
sys.setrecursionlimit(2000)


def __starting_point():
    n = [int(val) for val in sys.stdin.readline().split()][0]
    count = 0
    s = set([])
    while not n in s:
        s.add(n)
        n += 1
        n = str(n)
        while n[-1] == '0':
            n = n[:-1]
        n = int(n)
        count += 1
    print(count)


__starting_point()
