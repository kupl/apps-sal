import math
h = int(input())
l = int(math.log(h, 2))
p = 2 ** l * 2 - 1
print(p)
