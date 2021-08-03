import math
import sys
from collections import Counter, defaultdict, deque
from sys import stdin, stdout
input = stdin.readline
def li(): return list(map(int, input().split()))


def solve():
    n = int(input())
    a = li()
    b = li()
    a.sort()
    b.sort()
    print(*a)
    print(*b)


for _ in range(int(input())):
    solve()
