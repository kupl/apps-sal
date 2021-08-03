import math
import sys
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
input = stdin.readline
def I(): return int(input())


def li(): return list(map(int, input().split()))


def case():
    n = input().strip()
    ans = []
    for i in range(len(n)):
        if(n[i] != "0"):
            ans.append(n[i] + "0" * (len(n) - i - 1))
    print(len(ans))
    print(*ans)


for _ in range(int(input())):
    case()
