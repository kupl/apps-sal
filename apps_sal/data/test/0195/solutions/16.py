(a, b, c, n) = [int(item) for item in input().split()]
if a + b - c > n - 1 or c > min(a, b):
    print(-1)
else:
    print(n - a - b + c)
