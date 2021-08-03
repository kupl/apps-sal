import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations
def input(): return sys.stdin.readline().rstrip()
def read(): return list(map(int, input().split()))
def go(): return 1 / 0


def write(*args, sep="\n"):
    for i in args:
        sys.stdout.write("{}{}".format(i, sep))


INF = float('inf')
MOD = int(1e9 + 7)
YES = "YES"
NO = "NO"

for _ in range(int(input())):
    try:
        a, b, c, n = read()
        x = max([a, b, c])
        n -= x - a
        n -= x - b
        n -= x - c

        if n < 0:
            print(NO)
            go()

        if n % 3 == 0:
            print(YES)
        else:
            print(NO)

    except:
        continue
