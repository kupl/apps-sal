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

for _ in range(1):
    try:
        n = int(input())
        a = read()
        b = read()
        x = 0
        y = 0

        for i in range(n):
            if a[i] == 0 and b[i] == 1:
                y += 1
            elif a[i] == 1 and b[i] == 0:
                x += 1

        if x == 0:
            print(-1)
            go()
        else:
            print(y // x + 1)

    except ZeroDivisionError:
        continue

    except Exception as e:
        print(e)
        continue
