import math
import sys
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
input = stdin.readline
def I(): return int(input())


def li(): return list(map(int, input().split()))


def case():
    a, b = li()
    print(a + b)


for _ in range(int(input())):
    case()
