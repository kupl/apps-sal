(a, b) = input().split()
a = int(a)
b = int(b)
if a % (b * 2 + 1) == 0:
    print(a // (b * 2 + 1))
else:
    print(a // (b * 2 + 1) + 1)
