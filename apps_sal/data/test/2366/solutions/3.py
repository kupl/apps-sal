from collections import Counter
from math import factorial


def nCr(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
D = dict()
s = 0
for a in set(A):
    c = C[a]
    if c > 1:
        x = nCr(c, 2)
        s += x
        if c > 2:
            D[a] = (x, nCr(c - 1, 2))
        else:
            D[a] = (x, 0)
    else:
        D[a] = (0, 0)

for a in A:
    t = D[a]
    print((s - t[0] + t[1]))

