from math import sqrt
from math import ceil


r, x, y, x2, y2 = list(map(int, input().split()))

print(ceil(sqrt((x-x2)**2+(y-y2)**2) / (2*r)))




