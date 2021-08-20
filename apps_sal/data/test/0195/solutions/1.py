(a, b, c, n) = list(map(int, input().split()))
if c > a or c > b or n - (a + b - c) < 1:
    print(-1)
else:
    print(n - (a + b - c))
