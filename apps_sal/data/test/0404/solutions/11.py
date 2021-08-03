from math import sqrt
b = int(input())
n = 0
r = int(sqrt(b))
for i in range(1, r + 1):
    if b % i == 0:
        n += 1
n *= 2
if r * r == b:
    n -= 1
print(n)
