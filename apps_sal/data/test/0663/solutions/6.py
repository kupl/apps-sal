import math
r, x, y, x1, y1 = map(int, input().split())
ln = math.sqrt((x-x1)**2 + (y-y1)**2)
print(math.ceil(ln/(2*r)))
