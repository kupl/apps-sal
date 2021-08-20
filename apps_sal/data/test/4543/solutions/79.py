import math
(a, b) = input().split()
if math.sqrt(int(a + b)).is_integer():
    print('Yes')
else:
    print('No')
