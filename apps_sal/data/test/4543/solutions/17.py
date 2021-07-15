import math

a, b = input().split()
s = a + b
i = int(s)
r = math.sqrt(i)
if r.is_integer():
    print("Yes")
else:
    print("No")
