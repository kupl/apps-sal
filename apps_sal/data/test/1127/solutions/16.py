import math
import sys
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
input = stdin.readline
I = lambda: int(input())
li = lambda: list(map(int, input().split()))


def solve():
    n = I()
    s = input().strip()
    if(n % 2):
        f = 2
        for i in range(0, n, 2):
            if(int(s[i]) % 2):
                f = 1
        print(f)
    else:
        f = 1
        for i in range(1, n, 2):
            if(int(s[i]) % 2 == 0):
                f = 2
        print(f)


for _ in range(I()):
    solve()
