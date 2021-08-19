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
    try:
        (n, g, b) = read()
        total = math.ceil(n / 2)
        s = 0
        e = 1 << 63
        while s <= e:
            m = (s + e) // 2
            good = 0
            bad = 0
            x = m // (g + b)
            good += x * g
            bad += x * b
            y = m - m // (g + b) * (g + b)
            good += min(y, g)
            bad += max(0, y - g)
            if good + bad >= n and good >= total:
                e = m - 1
            else:
                s = m + 1
        print(s)
    except ZeroDivisionError:
        continue
    except Exception as e:
        print(e)
        continue
