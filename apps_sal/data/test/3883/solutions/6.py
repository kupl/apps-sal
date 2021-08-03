import math
a, b = map(float, input().split())
print(-1 if b > a else(((a + b) / 2) / math.floor(((a + b) / 2) / b)))
