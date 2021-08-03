import math
n = int(input())
a = int(math.sqrt(n))
if a * a < n:
    a += 1
b = math.ceil(n / a)
print(a + b)
