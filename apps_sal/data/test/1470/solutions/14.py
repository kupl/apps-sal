import math
x = int(input())
if 1 <= x % 11 <= 6:
    print(math.ceil(x / 11) * 2 - 1)
else:
    print(math.ceil(x / 11) * 2)
