import math
n = int(input())
l = math.floor(math.sqrt(n))
for i in range(1, l + 1):
    if n % i == 0:
        x = i
        y = n // i
print(x - 1 + (y - 1)) if x > 0 else print(n - 1)
