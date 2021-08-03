from itertools import accumulate
from math import gcd

N = int(input())
A = list(map(int, input().split()))

l = list(accumulate(A[:-1], gcd, initial=0))
r = list(accumulate(A[::-1], gcd, initial=0))
print(max(gcd(l[i], r[N - i - 1]) for i in range(N)))
