import math
x = int(input())
a = 100
year = 0
for i in range(10 ** 10):
    a += a // 100
    year += 1
    if a >= x:
        break
print(year)
