from math import sqrt, ceil
n = int(input())
a = ceil(sqrt(n))
for i in range(a, n + 1):
    if n % i == 0:
        print(n // i, i)
        return
