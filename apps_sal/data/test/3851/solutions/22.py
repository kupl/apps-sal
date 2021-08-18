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
def mul(): return map(int, input().strip().split())
def mulf(): return map(float, input().strip().split())
def seq(): return list(map(int, input().strip().split()))


def ceil(x): return int(x) if (x == int(x)) else int(x) + 1
def ceildiv(x, d): return x // d if (x % d == 0) else x // d + 1


def flush(): return stdout.flush()
def stdstr(): return stdin.readline()
def stdint(): return int(stdin.readline())
def stdpr(x): return stdout.write(str(x))
def stdarr(): return map(int, stdstr().split())


mod = 1000000007


n, k = stdarr()
a, b = stdarr()

second = 1 + a

l = set()

for i in range(k + 1, n * k + 1, k):
    l.add((i - b - second) % (n * k + 1))
    l.add((i + b - second) % (n * k + 1))

l.add((n * k - b - second + 1))
l.add((n * k + b - second + 1))

x = float('inf')
y = -1


for i in l:
    if(i == 0):
        continue
    if((n * k) % i == 0):
        d = (n * k) // i
    else:
        lcm = (i * (n * k)) // math.gcd(i, n * k)
        d = lcm // i

    x = min(d, x)
    y = max(d, y)

print(x, y)
