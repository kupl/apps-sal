import math
(a, b) = input().split()
c = int(a + b)
d = math.sqrt(c)
e = math.floor(d)
if e ** 2 == c:
    print('Yes')
else:
    print('No')
