import math
(a, b) = list(map(str, input().split()))
target = math.sqrt(int(a + b))
if target.is_integer():
    print('Yes')
else:
    print('No')
