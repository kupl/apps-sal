(a, b, c, d) = map(int, input().split())
x = a * b
y = c * d
if x >= y:
    print(x)
if y > x:
    print(y)
