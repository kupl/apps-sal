a, b = input().split()
a = int(a)
b = int(b)
c = a * (b + b + a - 1) / 2
if b > 0:
    print(int(c - b))
else:
    if b + a - 1 > 0:
        print(int(c))
    else:
        print(int(c - (b + a - 1)))
