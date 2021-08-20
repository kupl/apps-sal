import math
h = int(input())
x = math.floor(math.log2(h)) + 1
y = 2 ** x - 1
print(y)
