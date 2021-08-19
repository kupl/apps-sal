def main():
    input()
    l = list(map(int, input().split()))
    a = l[-1]
    while not a % 2:
        a //= 2
    while not a % 3:
        a //= 3
    for x in l:
        while not x % 2:
            x //= 2
        while not x % 3:
            x //= 3
        if x != a:
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
