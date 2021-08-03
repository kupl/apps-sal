import math

n, r = list(map(int, input().split()))
print(n * r * r / (1 / math.tan(math.pi / (2 * n)) + 1 / math.tan(math.pi / n)))
