import math

N = int(input())

p = 1
for i in range(2, N + 1):
    p *= i
    p = p % (1000000000 + 7)

print(p)
