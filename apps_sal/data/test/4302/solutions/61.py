a, b = list(map(int, input().split()))
if a == b:
    print((2 * a))
elif a > b:
    print((2 * a - 1))
else:
    print((2 * b - 1))
