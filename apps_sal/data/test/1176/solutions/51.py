def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    aa = sorted(abs(i) for i in a)

    if sum(i < 0 for i in a) % 2 == 0:
        print(sum(aa))
    else:
        print(-aa[0] + sum(aa[1:]))


def __starting_point():
    main()


__starting_point()
