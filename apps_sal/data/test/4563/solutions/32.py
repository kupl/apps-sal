from decimal import Decimal, getcontext
from math import ceil

N = int(input())

takahashi, aoki = 1, 1

for _ in range(N):
    a, b = map(int, input().split())
    c = max(ceil(takahashi / Decimal(a)), ceil(aoki / Decimal(b)))
    takahashi = c * a
    aoki = c * b

print(takahashi + aoki)
