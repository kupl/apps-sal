from sys import stdin, stdout
import math
from collections import Counter, defaultdict
LI = lambda: list(map(int, input().split()))
MAP = lambda: list(map(int, input().split()))
IN = lambda: int(input())
S = lambda: input()


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
