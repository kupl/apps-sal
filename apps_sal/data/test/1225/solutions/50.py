import math

h = int(input())
n = math.floor(math.log2(h)) + 1

print(2 ** n - 1)
