import math as mt
n = int(input())
lst = [int(input()) for i in range(5)]
print(mt.ceil(n / min(lst)) + 4)
