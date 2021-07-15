import math

n = int(input())
capa = [int(input()) for _ in range(5)]

print(4 + math.ceil(n / min(capa)))
