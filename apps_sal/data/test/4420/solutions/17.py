t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())

    ma = (n // x) * x

    if ma + y <= n:
        ans = ma + y
    else:
        ans = ma - x + y

    print(ans)
