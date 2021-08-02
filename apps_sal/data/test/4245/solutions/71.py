import math

A, B = map(int, input().split())
N = math.ceil((B - A) / (A - 1) + 1)

print(N)
