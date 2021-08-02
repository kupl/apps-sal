a, b = map(int, input().split())

if a <= b:
    print(0)
elif a - 2 * b <= 0:
    print(0)
elif a - 2 * b > 0:
    print(a - 2 * b)
