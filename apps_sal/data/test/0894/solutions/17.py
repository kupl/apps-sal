(a, b) = input().split()
x = int(a)
y = int(b)
if x > 0 and y > 0:
    print(0, x + y, x + y, 0)
elif x > 0 and y < 0:
    print(0, -(abs(y) + x), abs(y) + x, 0)
elif x < 0 and y > 0:
    print(-(abs(x) + y), 0, 0, abs(x) + y)
elif x < 0 and y < 0:
    print(x + y, 0, 0, x + y)
