import sys
import math
from collections import Counter


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

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
