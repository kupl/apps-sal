import math
a = int(input())
n = 0
if a > 0:
    b = int(math.sqrt(a ** 2 / 2))
    if b ** 2 + (b + 1) ** 2 <= a ** 2:
        n = b * 8 + 4
    else:
        n = b * 8
    print(n)
else:
    print('1')
