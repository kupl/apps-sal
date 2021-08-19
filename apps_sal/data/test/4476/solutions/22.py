for _ in range(int(input())):
    (a, b) = map(int, input().split())
    if a == b:
        print(0)
    elif a > b:
        h = a - b
        if h % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        h = b - a
        if h % 2 == 1:
            print(1)
        else:
            print(2)
