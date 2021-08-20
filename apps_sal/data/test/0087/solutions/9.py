from math import ceil
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
(m, d) = list(map(int, input().split()))
print(ceil((months[m] + d - 1) / 7))
