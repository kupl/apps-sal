import math
n = int(input())
num = int(math.ceil(float(n) / 1000))
print(num * 1000 - n)
