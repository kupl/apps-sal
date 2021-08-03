for i in range(int(input())):
    n = int(input())
    times = 0
    canDo = True
    while (n != 1):
        if n % 6 == 0:
            n = n // 6
        elif n % 3 == 0:
            n *= 2
        else:
            canDo = False
            break
        times += 1
    if canDo:
        print(times)
    else:
        print("-1")
