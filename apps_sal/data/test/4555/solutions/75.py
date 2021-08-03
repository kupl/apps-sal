a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a + c - 1) < (b - c + 1):
    for i in range(c):
        print(a + i)
    for i in range(c):
        print(b - c + 1 + i)
else:
    for i in range(a, b + 1):
        print(i)
