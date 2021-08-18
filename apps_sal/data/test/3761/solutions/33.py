from collections import Counter
from itertools import product
def inpl(): return tuple(map(int, input().split()))


S = input()
x, y = inpl()
M = []

d = 0
for s in S:
    if s == "F":
        d += 1
    else:
        M.append(d)
        d = 0
M.append(d)

Cx = Counter(M[2::2])
Cy = Counter(M[1::2])

Lx = []
Ly = []

for k, v in Cx.items():
    if k == 0:
        pass
    else:
        Lx.append(list(range(-k * v, k * v + 1, 2 * k)))

for k, v in Cy.items():
    if k == 0:
        pass
    else:
        Ly.append(list(range(-k * v, k * v + 1, 2 * k)))


def bfss(Ls, t, f):
    N = set([f])
    for L in Ls:
        nN = set()
        nN.update([n + l for n, l in product(N, L)])
        N = nN
    if t in N:
        return True
    else:
        return False


if bfss(Lx, x, M[0]) and bfss(Ly, y, 0):
    print("Yes")
else:
    print("No")
