import math
a = list(map(int, input().split()))
if a[0] == 1 and a[1] == 1:
    print(0)
elif a[0] == 0 or a[0] == 1:
    b = math.factorial(a[1]) / (math.factorial(2) * math.factorial(a[1] - 2))
    print(int(b))
elif a[1] == 0 or a[1] == 1:
    b = math.factorial(a[0]) / (math.factorial(2) * math.factorial(a[0] - 2))
    print(int(b))
else:
    b = math.factorial(a[1]) / (math.factorial(2) * math.factorial(a[1] - 2))
    c = math.factorial(a[0]) / (math.factorial(2) * math.factorial(a[0] - 2))
    print(int(b + c))
