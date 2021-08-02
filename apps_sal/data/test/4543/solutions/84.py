import math
a, b = list(map(int, input().split()))
c = 0

if b < 10:
    c = a * 10 + b
elif 10 <= b <= 99:
    c = a * 100 + b
elif b == 100:
    c = a * 1000 + b

d = math.sqrt(c)

if d.is_integer():
    print("Yes")
else:
    print("No")
