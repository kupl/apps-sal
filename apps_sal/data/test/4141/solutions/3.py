def main():
    n = int(input())
    a = [int(v) for v in input().split()]
    for i in range(len(a)):
        if a[i] % 2 == 0:
            if a[i] % 3 == 0 or a[i] % 5 == 0:
                continue
            else:
                return 'DENIED'
    return 'APPROVED'


def __starting_point():
    print(main())


__starting_point()
