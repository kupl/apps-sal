for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    if b >= a:
        print(b)
    elif d >= c:
        print('-1')
    else:
        print(b + c * ((a - b - 1) // (c - d) + 1))
