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
mul = lambda: map(int, input().strip().split())
mulf = lambda: map(float, input().strip().split())
seq = lambda: list(map(int, input().strip().split()))

ceil = lambda x: int(x) if (x == int(x)) else int(x) + 1
ceildiv = lambda x, d: x // d if (x % d == 0) else x // d + 1

flush = lambda: stdout.flush()
stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr = lambda x: stdout.write(str(x))
stdarr = lambda: map(int, stdstr().split())

mod = 1000000007


n,k = stdarr()
a,b = stdarr()

second = 1+a

l = set()

for i in range(k+1, n*k+1, k):
    l.add((i-b-second)%(n*k + 1))
    l.add((i+b-second)%(n*k + 1))

l.add((n*k - b - second + 1))
l.add((n*k + b - second + 1))

x = float('inf')
y = -1


for i in l:
    if(i == 0): continue
    if((n*k)%i == 0):
        d = (n*k)//i
    else:
        lcm = (i*(n*k))//math.gcd(i, n*k)
        d = lcm//i

    x = min(d, x)
    y = max(d, y)

print(x, y)
