def main():
    (p, n) = list(map(int, input().split()))
    table = set()
    for i in range(1, n + 1):
        x = int(input())
        if x % p in table:
            print(i)
            return
        else:
            table.add(x % p)
    print(-1)
    return


def __starting_point():
    main()


__starting_point()
