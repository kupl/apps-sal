import math
import sys
from collections import Counter, defaultdict, deque
from sys import stdin, stdout
input = stdin.readline


def li():
    return list(map(int, input().split()))


def case():
    (n, m) = li()
    a = li()
    s = sum(a)
    print(min(s, m))


for _ in range(int(input())):
    case()
