from math import sqrt, ceil
(r, x, y, xx, yy) = map(int, input().split())
diff = sqrt((x - xx) ** 2 + (y - yy) ** 2)
print(ceil(ceil(diff) / (r * 2)))
