import math

a, b = map(int, input().split())
x = int(str(a) + str(b))
if math.sqrt(x) == math.ceil(math.sqrt(x)):
    print("Yes")
else:
    print("No")
