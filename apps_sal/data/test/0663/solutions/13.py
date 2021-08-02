import math

r, x0, y0, x1, y1 = list(map(int, input().split()))
print(math.ceil(math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) * .5 / r))
