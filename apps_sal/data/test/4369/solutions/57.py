import math
n = int(input())
if n % 2 == 0:
    print(math.floor(n / 2))
else:
    n = n + 1
    print(math.floor(n / 2))
