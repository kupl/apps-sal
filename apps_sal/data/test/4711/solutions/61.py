(a, b, c) = map(int, input().split())
x = a + b
y = b + c
z = c + a
if x <= y and x <= z:
    print(x)
elif y <= x and y <= z:
    print(y)
else:
    print(z)
