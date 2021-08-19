(a, b, c, n) = list(map(int, input().split()))
passed = a + b - c
if c > a or c > b or passed > n - 1:
    print(-1)
else:
    print(n - passed)
