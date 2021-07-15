from math import ceil
n = int(input())
c = ceil(n ** 0.5)
print(c + (n + c - 1)//c)
