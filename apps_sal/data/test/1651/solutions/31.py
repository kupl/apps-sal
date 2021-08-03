import math
a, b = map(int, input().split())

p = a * a - 4 * b
q = math.sqrt(p)
q = math.floor(q)
if q * q == p:
    print("Yes")
else:
    print("No")
