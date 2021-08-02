import math
x = int(input().replace(' ', ''))
y = int(math.sqrt(x))
if y * y == x:
    print("Yes")
else:
    print("No")
