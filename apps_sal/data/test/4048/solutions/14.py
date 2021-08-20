from math import sqrt
n = int(input())
minSoFar = 10 ** 12 + 1
for a in range(1, int(sqrt(n)) + 1):
    if n % a == 0:
        b = n // a
        minSoFar = min(minSoFar, a + b - 2)
print(minSoFar)
