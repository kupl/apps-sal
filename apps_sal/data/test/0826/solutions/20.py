from math import sqrt

n = int(input())
s = int(sqrt(2 * (n + 1)))
while s * (s + 1) <= 2 * (n + 1):
    s += 1
s -= 1
print(n - s + 1)
