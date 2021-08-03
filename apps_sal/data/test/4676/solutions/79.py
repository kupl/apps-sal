import math
a = input()
b = input()

n = ''
for i in range(len(a) + len(b)):
    if i % 2 == 0:
        n = n + a[i // 2]
    else:
        n = n + b[math.ceil(i / 2) - 1]
print(n)
