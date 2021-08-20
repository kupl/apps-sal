import math
(a, b) = input().split()
num = int(a + b)
if math.sqrt(num).is_integer():
    print('Yes')
else:
    print('No')
