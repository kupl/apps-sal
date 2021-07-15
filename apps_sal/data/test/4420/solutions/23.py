for _ in range(int(input())):
    x, y, n = map(int, input().split())
    if n % x < y:
        print(x * (n // x - 1) + y)
    else:
        print(x * (n // x) + y)
