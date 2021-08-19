for _ in range(int(input())):
    (a, b, c, d) = tuple(map(int, input().split()))
    if a <= b:
        print(b)
    elif c > d:
        a -= b
        t = (a - 1) // (c - d) + 1
        print(b + t * c)
    else:
        print(-1)
