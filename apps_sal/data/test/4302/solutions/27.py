a, b = list(map(int, input().split()))
if a == b:
    print((2 * a))
else:
    print((max(a, b) + max(a - 1, b - 1)))
