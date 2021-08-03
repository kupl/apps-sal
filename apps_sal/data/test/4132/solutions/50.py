# author:  Taichicchi
# created: 14.09.2020 22:18:44

import sys
from math import gcd

N = int(input())

A = list(map(int, input().split()))

ans = gcd(A[0], A[1])
for i in range(2, N):
    ans = gcd(ans, A[i])

print(ans)
