from functools import reduce
from math import gcd
N = int(input())
l = list(map(int, input().split()))
sw = 0
c = [0] * 1000001
for i in l:
    c[i] += 1
if all((sum(c[i::i]) <= 1 for i in range(2, 1000001))):
    print('pairwise coprime')
elif reduce(gcd, l) == 1:
    print('setwise coprime')
else:
    print('not coprime')
