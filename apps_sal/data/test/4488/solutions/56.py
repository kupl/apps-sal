import math
a = int(input())
b = int(input())
if math.sqrt(a) == math.sqrt(b):
    print("EQUAL")
elif math.sqrt(a) > math.sqrt(b):
    print("GREATER")
elif math.sqrt(a) < math.sqrt(b):
    print("LESS")
