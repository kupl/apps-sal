from math import sqrt, log10
n = int(input())

for i in reversed(range(int(sqrt(n)) + 1)):
    if n % i == 0:
        break
a = int(log10(i)) + 1
b = int(log10(n // i)) + 1
print(max(a, b))
