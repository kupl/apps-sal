import math
n = int(input())
maxval = n
i = 2
while i * i <= n:
    while maxval % (i * i) == 0:
        maxval //= i
    i += 1

print(maxval)
