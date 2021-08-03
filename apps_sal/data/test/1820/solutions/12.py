import sys
import math
from collections import Counter, defaultdict
input = sys.stdin.readline
def LI(): return list(map(int, input().split()))
def MAP(): return list(map(int, input().split()))
def IN(): return int(input())
def S(): return input()


def case():
    n = IN()
    a = LI()
    if a[0] + a[1] > a[-1]:
        print(-1)
    else:
        print(1, 2, n)


for _ in range(IN()):
    case()
