from collections import *
N = int(input())
C = Counter(input())
for n in range(N - 1):
    C &= Counter(input())
print(*sorted(C.elements()), sep='')
