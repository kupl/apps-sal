a, b, c, n = list(map(int, input().split()))
result = n - (a + b - c)
if result <= 0 or c > a or c > b or a > n or b > n:
    print(-1)
else:
    print(result)
