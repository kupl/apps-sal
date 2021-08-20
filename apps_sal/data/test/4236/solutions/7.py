import sys
import math
import random
from fractions import gcd
from itertools import permutations
debug = 0
if debug:
    f = open('input.txt', 'r')
    input = f.readline
else:
    input = sys.stdin.readline


def mp():
    return list(map(int, input().split()))


def _main():
    (n, m) = mp()
    a = [0] * n
    for i in range(n):
        a[i] = mp()
    ans = []
    for i in range(1, m + 1):
        t = False
        for j in a:
            if j[0] <= i and j[1] >= i:
                t = True
        if t == False:
            ans.append(i)
    print(len(ans))
    print(*ans)


_main()
