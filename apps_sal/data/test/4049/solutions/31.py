import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from collections import Counter

#sys.setrecursionlimit(100000000)

inp = lambda: int(input())
strng = lambda: input().strip()
jn = lambda x, l: x.join(map(str, l))
strl = lambda: list(input().strip())
mul = lambda: list(map(int, input().strip().split()))
mulf = lambda: list(map(float, input().strip().split()))
seq = lambda: list(map(int, input().strip().split()))

ceil = lambda x: int(x) if (x == int(x)) else int(x) + 1
ceildiv = lambda x, d: x // d if (x % d == 0) else x // d + 1

flush = lambda: stdout.flush()
stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr = lambda x: stdout.write(str(x))
stdarr = lambda: list(map(int, stdstr().split()))

mod = 1000000007

n = stdint()

a1,a2,a3 = stdarr()
b1,b2,b3 = stdarr()

mi = 0
ma = 0

#for max
wi = min(a1, b2)
re = max(a1-wi, 0)
draw = min(re, b1)
re = re-draw
lose = min(re, b3)

ma += wi

wi = min(a2, b3)
re = max(a2-wi, 0)
draw = min(re, b2)
re = re-draw
lose = min(re, b1)

ma += wi

wi = min(a3, b1)
re = max(a3-wi, 0)
draw = min(re, b3)
re = re-draw
lose = min(re, b2)

ma += wi

#for min

l1 = min(a1, b3)
re = max(a1-l1, 0)
draw = min(re, b1)
wi = min(re-draw, b2)


mi += wi

l1 = min(a2, b1)
re = max(a2-l1, 0)
draw = min(re, b2)
wi = min(re-draw, b3)

mi += wi

l1 = min(a3, b2)
re = max(a3-l1, 0)
draw = min(re, b3)
wi = min(re-draw, b1)

mi += wi

print(mi, ma)

