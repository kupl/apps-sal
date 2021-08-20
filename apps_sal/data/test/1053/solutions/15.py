from math import log
n = int(input()) - 1
divider = 2 ** int(log(n) / log(2))
total = 0
doubled = 0
while divider > 0:
    total += (n // divider - doubled) * divider
    doubled += n // divider - doubled
    divider //= 2
print(total)
