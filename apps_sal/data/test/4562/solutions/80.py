import math
n = int(input())
for i in range(10 ** 5):
    if n < i ** 2:
        print((i - 1) ** 2)
        break
