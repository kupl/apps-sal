def main():
    n = int(input())
    a = []
    if n == 4:
        print(4)
        print('2 4 1 3')
        return
    for i in range(0, n, 2):
        a.append(i + 1)
    if a[-1] != 1 and a[-1] != 3:
        for i in range(1, n, 2):
            a.append(i + 1)
    print(len(a))
    for i in range(len(a) - 1):
        print(a[i], end=' ')
    print(a[-1])


def __starting_point():
    main()


__starting_point()
