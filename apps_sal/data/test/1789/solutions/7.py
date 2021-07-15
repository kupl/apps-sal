import math
a, b, x, y = list(map(int, input().split()))

w = abs((2 * b) + 1 - (2 * a))
print((math.floor(w/2) * min(2 * x, y) + x))


