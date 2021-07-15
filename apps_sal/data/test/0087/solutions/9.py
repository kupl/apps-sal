months = [0, 31,28,31,30,31,30,31,31,30,31,30,31]

from math import ceil

m, d = list(map(int, input().split()))

print(ceil((months[m] + d - 1) / 7))

