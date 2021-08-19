(a, b, c) = input().split()
a = int(a)
b = int(b)
c = int(c)
if a >= c:
    print(a - c, b)
if a < c <= a + b:
    print(0, a + b - c)
if c > a + b:
    print(0, 0)
