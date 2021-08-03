from sys import stdin, stdout
import math
from collections import Counter, defaultdict
def LI(): return list(map(int, input().split()))
def MAP(): return list(map(int, input().split()))
def IN(): return int(input())
def S(): return input()


def case():
    n = IN()
    a = sorted(LI())
    for i in range(n - 1):
        if a[i + 1] - a[i] >= 2:
            print("NO")
            return
    print("YES")


for _ in range(IN()):
    case()
