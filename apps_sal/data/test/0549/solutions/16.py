import math
n = int(input())
for i in range(round(math.sqrt(n)), 0, -1):
    if n % i == 0:
        cols = n // i
        break
print(n // (n // i), end=' ')
print(n // i)
