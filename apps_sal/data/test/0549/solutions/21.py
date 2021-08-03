import math
n = int(input().strip())
for i in range(1, int(1 + math.sqrt(n))):
    if n % i == 0:
        p = i
p = min(p, n / p)
n = n // p
print(p, n)
