from itertools import product
from heapq import *

X, Y, Z, K, *f = map(int, open(0).read().split())
A = f[:X]
B = f[X:X + Y]
C = f[X + Y:]
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
AB = [sum(x) * (-1) for x in product(A, B)]
heapify(AB)
AB_picked = []
for i in range(K):
    if AB:
        AB_picked.append(heappop(AB) * (-1))
    else:
        break
ABC = [sum(x) * (-1) for x in product(AB_picked, C)]
heapify(ABC)
for i in range(K):
    print(heappop(ABC) * (-1))
