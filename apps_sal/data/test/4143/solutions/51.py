from math import ceil
n = int(input())
abcde = [int(input()) for _ in range(5)]
print(ceil(n/min(abcde))+4)
