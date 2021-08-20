def main():
    a = list(input())
    b = list(input()) + ['']
    for i in range(len(a)):
        print(a[i], end='')
        print(b[i], end='')


def __starting_point():
    main()


__starting_point()
