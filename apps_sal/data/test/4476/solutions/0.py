for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    if a == b:
        print(0)
    elif a < b:
        if (b - a) % 2:
            print(1)
        else:
            print(2)
    elif (b - a) % 2 == 0:
        print(1)
    else:
        print(2)
