for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    if b == a:
        print(0)
    elif b > a:
        if (b - a) % 2 == 0:
            print(2)
        else:
            print(1)
    elif (a - b) % 2 == 0:
        print(1)
    else:
        print(2)
