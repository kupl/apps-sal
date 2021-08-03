import math
a, b = map(int, input().split())
x = ""
y = 0
for i in range(a):
    x = input().split()
    if math.sqrt(int(x[0]) ** 2 + int(x[1]) ** 2) <= b:
        y = y + 1
print(y)
