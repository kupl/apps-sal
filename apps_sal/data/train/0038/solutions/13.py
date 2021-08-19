import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


def read():
    return list(map(int, input().split()))


def go():
    return 1 / 0


def write(*args, sep='\n'):
    for i in args:
        sys.stdout.write('{}{}'.format(i, sep))


INF = float('inf')
MOD = int(1000000000.0 + 7)
YES = 'YES'
NO = 'NO'
for _ in range(int(input())):
    (n, x, y) = read()
    X = read()
    Y = read()
    if n in X:
        print(YES)
    else:
        print(NO)
