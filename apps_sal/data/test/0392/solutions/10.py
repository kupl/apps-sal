import math
n = int(input())
res = 1
for i in range(2, round(math.sqrt(n)) + 1):
    if n % i == 0:
        res *= i
        while n % i == 0:
            n = n // i
if n != 0:
    res *= n
print(res)
