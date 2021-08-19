for _ in range(int(input())):
    (a, b) = map(int, input().split())
    x = 0
    y = 10 ** 10
    for i in input():
        if i == '0':
            (x, y) = (min(x, y), min(y + b, x + b + a))
        else:
            (x, y) = (10 ** 10, min(y, x + a))
    print(min(x, y))
