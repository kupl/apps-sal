import math as ma
a, b = map(int, input().split())
x = int(ma.sqrt(b)) + 1
f = False
for i in range(1, x):
    if b % i == 0:
        if (b // i) + i == a:
            f = True
            break
if f:
    print("Yes")
else:
    print("No")
