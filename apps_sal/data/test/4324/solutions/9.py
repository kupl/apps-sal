import math
import sys
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
input = stdin.readline


def I():
    return int(input())


def li():
    return list(map(int, input().split()))


def case():
    (n, a, b) = li()
    s = 'abcdefghijklmnopqrstuvwxyz'
    ans = []
    j = 0
    for i in range(n):
        ans.append(s[j])
        j += 1
        if j == b:
            j = 0
    print(''.join(map(str, ans)))


for _ in range(int(input())):
    case()
