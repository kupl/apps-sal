from math import sqrt
n = int(input())
k = int(sqrt(n))
s = 4 * k
if k * k < n:
    s += 2
    if k * (k + 1) < n:
        s += 2
print(s)
