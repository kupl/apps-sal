for t in range(int(input())):
    (a, b, c, d, k) = map(int, input().split())
    if (a - 1) // c + 1 + (b - 1) // d + 1 <= k:
        print((a - 1) // c + 1, (b - 1) // d + 1)
    else:
        print(-1)
