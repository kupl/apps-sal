from math import gcd
N = int(input())
r = 1
for i in range(2, N + 1):
    r = r / gcd(int(r), i) * i
print(int(r) + 1)
