a, b, c = list(map(int, input().split()))
if max(a, b, c) >= 2 * (a + b + c - max(a, b, c)):
    print(a + b + c - max(a, b, c))
else:
    print((a + b + c) // 3)
