import math
a = int(input())
b = []
for i in range(5):
    b.append(int(input()))
c = min(b)
d = math.ceil(a / c)
print(d + 4)
