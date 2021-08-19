def main():
    n = int(input())
    l = sorted(map(int, input().split()))
    res = 0
    while l:
        res += 1
        (i, l1) = (0, [])
        for x in l:
            if x < i:
                l1.append(x)
            else:
                i += 1
        l = l1
    print(res)


def __starting_point():
    main()


__starting_point()
