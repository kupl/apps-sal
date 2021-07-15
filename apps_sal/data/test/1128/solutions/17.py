import sys
import math
a, m = list(map(int, input().split()))

if a % m == 0 or 2*a % m == 0:
    print("Yes")
    return

a1 = a
f = False
for k in range(int(math.log(m, 2)) + 1):
    if a * (2 ** k) % m == 0:
        f = True
        break

if f:
    print("Yes")
else:
    print("No")

