from math import ceil
n = int(input())
a = [int(input()) for i in range(5)]
print(ceil(n / min(a)) - 1 + 5)
