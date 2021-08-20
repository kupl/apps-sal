for _ in range(int(input())):
    (x, y, a, b) = map(int, input().split())
    d = y - x
    if d % (a + b) == 0:
        print(d // (a + b))
    else:
        print(-1)
