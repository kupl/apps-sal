for _ in range(int(input())):
    x, y = tuple(map(int, input().split()))
    a, b = tuple(map(int, input().split()))

    if a * 2 <= b:
        print((x + y) * a)
    else:
        print(min(x, y) * b + (max(x, y) - min(x, y)) * a)
