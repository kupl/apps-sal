import sys
import math
from collections import Counter


def inint(): return int(sys.stdin.readline())
def inintm(): return map(int, sys.stdin.readline().split())
def inintl(): return list(inintm())
def instrm(): return map(str, sys.stdin.readline().split())
def instrl(): return list(instrm())


n = inint()
A = inintl()

C = Counter(A)
ans = 0

for c in C:
    if c > C[c]:
        ans += C[c]
    elif c < C[c]:
        ans += C[c] - c

print(ans)
