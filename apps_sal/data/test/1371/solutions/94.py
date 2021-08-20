def main():
    S = int(input())
    a = [1, 0, 0, 1, 1, 1, 2]
    for i in range(7, S + 1):
        a.append(sum(a[i - 3::-1]))
    print(a[S] % (10 ** 9 + 7))


def __starting_point():
    main()


__starting_point()
