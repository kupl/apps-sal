import itertools, bisect
from fractions import Fraction
from math import factorial


def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


N, A, B = list(map(int, input().split()))
V = sorted(list(map(int, input().split())), reverse=True)

Ave = [Fraction(a, i) for i, a in enumerate(itertools.accumulate(V), 1)]
max_num = max(Ave[A - 1:B])
max_indices = [i for i, v in enumerate(Ave) if A <= i + 1 <= B and v == max_num]

Vm = [-v for v in V]
C = 0
for ind in max_indices:
    l = bisect.bisect_left(Vm, Vm[ind])
    r = bisect.bisect_right(Vm, Vm[ind])
    C += comb(r - l, ind - l + 1)
print((float(max_num)))
print(C)

