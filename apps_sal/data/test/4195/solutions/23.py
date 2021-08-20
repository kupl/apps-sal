(a, b) = input().split()
a = int(a)
b = int(b)
if b < 100:
    print(100 ** a * b)
elif b == 100:
    print(100 ** a * (b + 1))
