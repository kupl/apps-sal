n = int(input())
*li,=list(map(int, input().split()))
from collections import Counter
c = Counter()
for i in li:
    c[i] += 1
ans=0
from math import comb
for i in list(c.values()):
    ans += comb(i, 2)
for i in li:
    print((ans - comb(c[i], 2) + comb(c[i]-1, 2)))

