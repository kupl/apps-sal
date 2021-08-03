__author__ = 'Utena'
import math
n = int(input())
i = int(math.sqrt(n * 2))
c = 0
while True:
    c = i * (i + 1) // 2
    if c >= n:
        break
    else:
        i += 1
print(n - c + i)
