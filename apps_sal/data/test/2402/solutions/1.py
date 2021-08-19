t = int(input())
for _ in range(t):
    (n, x, y) = [int(item) for item in input().split()]
    total = x + y
    maximum = min(x + y - 1, n)
    minimum = min(n - min(2 * n - total, n) + 1, n)
    print(minimum, maximum)
