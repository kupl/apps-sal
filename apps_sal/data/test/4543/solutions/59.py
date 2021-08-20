import math
(a, b) = input().split()
c = int(a + b)
d = math.sqrt(c)
print('Yes' if d == int(d) else 'No')
