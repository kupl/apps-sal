import sys
import math
n = int(input())
comba = []
for _ in range(n):
    (a, b) = map(int, input().split())
    suma = a + b
    comba.append(suma)
print(max(comba))
