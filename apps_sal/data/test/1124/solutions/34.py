from sys import stdin, stdout
from collections import *
from math import ceil, floor, log, gcd
st = lambda: list(stdin.readline().strip())
li = lambda: list(map(int, stdin.readline().split()))
mp = lambda: list(map(int, stdin.readline().split()))
inp = lambda: int(stdin.readline())
pr = lambda n: stdout.write(str(n) + "\n")

mod = 1000000007
INF = float('inf')


def solve():
    n = inp()
    l = li()
    g = l[0]
    for i in range(1, n):
        g = gcd(g, l[i])
    pr(g)


for _ in range(1):
    solve()
