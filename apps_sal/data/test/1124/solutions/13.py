from functools import reduce
import math
a = int(input())
b = list(map(int, input().split()))
GCD = b[0]
for c in b:
    GCD = math.gcd(c, GCD)
print(GCD)
