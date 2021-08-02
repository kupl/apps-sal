a, b = map(int, input().split())

if a <= 2 * b:
    print(0)
else:
    print(a - 2 * b)
