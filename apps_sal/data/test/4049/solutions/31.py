import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from collections import Counter


def inp(): return int(input())
def strng(): return input().strip()
def jn(x, l): return x.join(map(str, l))
def strl(): return list(input().strip())
def mul(): return list(map(int, input().strip().split()))
def mulf(): return list(map(float, input().strip().split()))
def seq(): return list(map(int, input().strip().split()))


def ceil(x): return int(x) if (x == int(x)) else int(x) + 1
def ceildiv(x, d): return x // d if (x % d == 0) else x // d + 1


def flush(): return stdout.flush()
def stdstr(): return stdin.readline()
def stdint(): return int(stdin.readline())
def stdpr(x): return stdout.write(str(x))
def stdarr(): return list(map(int, stdstr().split()))


mod = 1000000007

n = stdint()

a1, a2, a3 = stdarr()
b1, b2, b3 = stdarr()

mi = 0
ma = 0

wi = min(a1, b2)
re = max(a1 - wi, 0)
draw = min(re, b1)
re = re - draw
lose = min(re, b3)

ma += wi

wi = min(a2, b3)
re = max(a2 - wi, 0)
draw = min(re, b2)
re = re - draw
lose = min(re, b1)

ma += wi

wi = min(a3, b1)
re = max(a3 - wi, 0)
draw = min(re, b3)
re = re - draw
lose = min(re, b2)

ma += wi


l1 = min(a1, b3)
re = max(a1 - l1, 0)
draw = min(re, b1)
wi = min(re - draw, b2)


mi += wi

l1 = min(a2, b1)
re = max(a2 - l1, 0)
draw = min(re, b2)
wi = min(re - draw, b3)

mi += wi

l1 = min(a3, b2)
re = max(a3 - l1, 0)
draw = min(re, b3)
wi = min(re - draw, b1)

mi += wi

print(mi, ma)
