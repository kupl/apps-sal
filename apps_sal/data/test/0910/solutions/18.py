(n, a, b) = list((int(x) for x in input().split(' ')))


def parlament(n, a, b):
    if n > a * b:
        print(-1)
        return 0
    if n >= b:
        up = list(range(1, b + 1))
        current = list(range(1, b + 1))
    else:
        up = list(range(1, n + 1))
        current = list(range(1, n + 1))
        for x in range(b - n):
            current.append(0)
    print(*current)
    current = list()
    chet = b - b % 2
    nechet = b - 1 + (b - chet) + 2
    chet += 2
    for i in range(a - 1):
        for j in range(b):
            if nechet <= n and up[j] % 2 == 0:
                print(nechet, end=' ')
                current.append(nechet)
                nechet = nechet + 2
            elif chet <= n and up[j] % 2 != 0:
                print(chet, end=' ')
                current.append(chet)
                chet = chet + 2
            else:
                print(0, end=' ')
        up = list(current)
        current = list()
        print()


parlament(n, a, b)
