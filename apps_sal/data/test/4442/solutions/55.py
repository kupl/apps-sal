a, b = map(int, input().split())

if a > b:
    b = str(b)
    print(b * a)
else:
    a = str(a)
    print(a * b)
