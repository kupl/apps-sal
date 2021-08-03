for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    x, y = (a + c - 1) // c, (b + d - 1) // d
    if x + y <= k:
        print(x, y)
    else:
        print(-1)
