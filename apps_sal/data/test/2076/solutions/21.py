import sys
import math
from collections import defaultdict
from itertools import combinations
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


def read():
    return list(map(int, input().split()))


def write(*args, sep='\n'):
    for i in args:
        sys.stdout.write('{}'.format(i) + sep)


INF = float('inf')
MOD = int(1000000000.0 + 7)
for _ in range(int(input())):
    (a, b, c) = read()
    x = min(b, c // 2)
    b -= x
    y = min(a, b // 2)
    print(3 * x + 3 * y)
