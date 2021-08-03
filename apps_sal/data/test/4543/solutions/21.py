import math
a, b = input().split()
n = int(a + b)
if math.sqrt(n) % 1 == 0:
    print('Yes')
else:
    print('No')
