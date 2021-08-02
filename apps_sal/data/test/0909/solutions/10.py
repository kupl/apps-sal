a = int(input())
b = int(input())
c = int(input())
if a == 1:
    print(max((a + b) * c, a + b + c))
elif b == 1:
    print(max([(a + b) * c, a * (b + c), a + b + c]))
elif c == 1:
    print(max(a * (b + c), a + b + c))
else:
    print(a * b * c)
