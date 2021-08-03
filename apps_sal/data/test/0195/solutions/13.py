a, b, c, n = map(int, input().split())
if a + b - c >= n:
    print(-1)
elif a < c or b < c:
    print(-1)
else:
    print(n - (a + b - c))
