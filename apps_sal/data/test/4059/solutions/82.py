import math
n = int(input())
summ = 0
for i in range(1, n):
    summ += (n - 1) // i
print(summ)
