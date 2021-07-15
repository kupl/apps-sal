a, b = map(int, input().split())

if a <= b:
    print(str(a) * b)
elif a > b:
    print(a * str(b))
