import math
a = input()
x = ""
for i in range(math.ceil(len(a) / 2)):
    x += a[i * 2]
print(x)
