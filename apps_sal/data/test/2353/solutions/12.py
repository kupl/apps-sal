for _ in range(int(input())):
    (a, b, c, d) = [int(x) for x in input().split()]
    if b >= a:
        print(b)
    elif d >= c:
        print(-1)
    else:
        print(b + c * ((a - b + c - d - 1) // (c - d)))
