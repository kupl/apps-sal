import math
a, b = input().split()
a1 = int(a)
b1 = int(b)
x = math.floor((a1 + b1) / 2)
y = a1 - x
print(str(x) + " " + str(y))
