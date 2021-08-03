for i in range(int(input())):
    a, b, x, y, n = (int(j) for j in input().split())
    ans = 10 ** 18

    d1 = a - x
    d2 = b - y
    if (d1 > n):
        ans = min(ans, (a - n) * b)
    elif (d1 + d2 > n):
        ans = min(ans, x * (b - n + d1))
    else:
        ans = min(ans, x * y)

    x, y = y, x
    a, b = b, a

    d1 = a - x
    d2 = b - y
    if (d1 > n):
        ans = min(ans, (a - n) * b)
    elif (d1 + d2 > n):
        ans = min(ans, x * (b - n + d1))
    else:
        ans = min(ans, x * y)

    print(ans)
