a, b = list(map(int, input().split()))
if b > a:
    print(-1)
else:
    x1 = a + b
    x = b
    print(x1 / (2 * (x1 // (2 * x))))
