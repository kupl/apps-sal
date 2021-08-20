from math import sqrt, ceil
n = int(input())
m = ceil((-1 + sqrt(8 * n + 9)) / 2)
s = m * (m + 1) - 2 * (n + 1)
while s > 0:
    m -= 1
    s = m * (m + 1) - 2 * (n + 1)
print(n - m + 1)
