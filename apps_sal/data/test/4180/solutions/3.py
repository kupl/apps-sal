from math import ceil

N = int(input())

x = ceil(N / 1000)
print(x * 1000 - N)
