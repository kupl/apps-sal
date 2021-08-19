def main():
    a = input()
    b = input()
    for i in range(len(a)):
        print(a[i], end='')
        if i < len(b):
            print(b[i], end='')
    print()


def __starting_point():
    main()


__starting_point()
