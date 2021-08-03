a, b = input().split()
a = int(a)
b = int(b)
if b % 2 == 0:
    print(1 + (a - b) // 2)
else:
    print(1 + b // 2)
