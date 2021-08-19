(a, b, c) = input().split()
a = int(a)
b = int(b)
c = int(c)
i = 0
while i < 10:
    i = i + 1
    c = a * c - b
    print(c)
