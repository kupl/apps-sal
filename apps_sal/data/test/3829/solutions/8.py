import math
m, n = map(int, input().split(' '))

a = 0
b = 0
o = 0
for i in range(m):
    a = ((i + 1) / m) ** n;
    o = o + (a - b) * (i + 1)
    b = a
print(o)
