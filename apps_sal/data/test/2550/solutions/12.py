from math import ceil, sqrt, gcd, log, floor
from collections import deque
def ii(): return int(input())
def si(): return input()
def mi(): return map(int, input().strip().split(" "))
def li(): return list(mi())
def msi(): return map(str, input().strip().split(" "))
def lsi(): return list(msi())


for _ in range(ii()):
    n, m = mi()
    a = li()
    s = a[0] + sum(a[1:])
    print(min(s, m))
