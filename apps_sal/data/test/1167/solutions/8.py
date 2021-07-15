for _ in range(int(input())):
    a, b, c, d, k = list(map(int, input().split()))
    x = (a - 1) // c + 1
    y = (b - 1) // d + 1
    if y + x <= k:
        print(x, y)
    else:
        print(-1)

