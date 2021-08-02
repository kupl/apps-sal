import math
import sys
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
input = stdin.readline
def I(): return int(input())


def li(): return list(map(int, input().split()))


def solve():
    n = I()
    a = []
    d = defaultdict(int)
    for i in range(n):
        s = input().strip()
        for j in s:
            d[j] += 1
    flag = 1
    for i in d:
        if(d[i] % n):
            flag = 0
    if(flag):
        print("YES")
    else:
        print("NO")


for _ in range(I()):
    solve()
