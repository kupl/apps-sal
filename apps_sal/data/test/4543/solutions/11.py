import math
(a, b) = map(int, input().split())
ab = str(a) + str(b)
if math.sqrt(int(ab)) % 1 == 0:
    print('Yes')
else:
    print('No')
