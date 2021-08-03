a, b = input().split()
a = int(a)
b = int(b)
if a - b >= 2:
    print(2 * a - 1)
if b - a >= 2:
    print(2 * b - 1)
if -2 < a - b < 2:
    print(a + b)
