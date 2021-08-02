def main():
    [n, a, b] = [int(i) for i in input().split()]
    s = [int(i) for i in input().split()]
    sumAll = 0
    for i in range(n):
        sumAll += s[i]
    rest = s[1:]
    rest.sort(reverse=True)
    thresh = sumAll - s[0] * a / b
    i = 0
    sumBlocked = 0
    while sumBlocked < thresh:
        sumBlocked += rest[i]
        i += 1
    print(i)


def __starting_point():
    main()


__starting_point()
