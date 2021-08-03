a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if b <= c:
    if a + b >= c:
        print(0)
    else:
        print(c - b - a)
else:
    if a + c >= b:
        print(0)
    else:
        print(b - c - a)
