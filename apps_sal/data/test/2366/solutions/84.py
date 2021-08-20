from collections import Counter
from scipy.special import comb
s = input()
A = list(map(int, input().split()))
d = Counter(A)
sum_c = 0
for v in d.values():
    if v >= 2:
        sum_c += comb(v, 2, exact=True)
for a in A:
    x = sum_c - comb(d[a], 2, exact=True) + comb(d[a] - 1, 2, exact=True)
    print(x)
