n, k = list(map(int, input().split()))


a = [int(s) for s in input().split()]

from math import sqrt
from math import ceil

p = ceil((sqrt(1 + 8*k) - 1) / 2)

print(a[k - p*(p-1)//2 - 1])

