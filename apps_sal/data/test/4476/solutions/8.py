t = int(input())
while t:
    t += -1
    (a, b) = map(int, input().split())
    if b == a:
        print(0)
    elif b > a:
        if (b - a) % 2:
            print(1)
        else:
            print(2)
    elif (a - b) % 2:
        print(2)
    else:
        print(1)
