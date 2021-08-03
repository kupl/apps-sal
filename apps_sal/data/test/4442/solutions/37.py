a, b = map(int, input().split())

if a > b:
    print(str(b) * a)
elif a < b:
    print(str(a) * b)
else:
    print(str(a) * a)
