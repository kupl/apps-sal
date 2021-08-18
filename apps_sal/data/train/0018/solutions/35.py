import sys
import math


def pprint(s): return print(' '.join(map(str, s)))
def input(): return sys.stdin.readline().strip()


ipnut = input
for i in range(int(input())):
    n = int(input())
    print(1 / math.tan(math.pi / (2 * n)))
"""
10
10 11 12 13 14 15 16 17 11 11
"""
