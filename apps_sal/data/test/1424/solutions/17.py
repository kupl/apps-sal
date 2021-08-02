def main():
    n, m, k = list(map(int, input().split()))

    a = []
    for _ in range(m):
        a.append(int(input()))

    f = int(input())

    def bitcnt(i):
        c = 0
        while i:
            i &= i - 1
            c += 1
        return c

    res = 0
    for ai in a:
        if bitcnt(ai ^ f) <= k:
            res += 1
    print(res)


def __starting_point():
    main()


__starting_point()
