import math
a, b = map(str, input().split())
A = int(a + b)

if math.sqrt(A).is_integer() == True:
    print("Yes")
else:
    print("No")
