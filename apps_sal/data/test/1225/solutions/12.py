import math

h = int(input())
print(2 ** (math.floor(math.log2(h)) + 1) - 1)
