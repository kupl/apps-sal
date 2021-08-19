# author:  Taichicchi
# created: 12.09.2020 19:50:20

from collections import Counter
import sys

N = int(input())

A = list(map(int, input().split()))


c = Counter(A)

for i in range(N):
    print((c[i + 1]))
