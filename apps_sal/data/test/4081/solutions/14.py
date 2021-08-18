3


def main():
    input()
    a = [int(x) for x in input().split(' ')]
    n = len(a)

    l, r = 0, n - 1
    res = []

    last = 0
    picked = True

    while l <= r and picked:
        picked = False
        if last < a[l] and last < a[r]:
            if a[l] < a[r]:
                last = a[l]
                res.append('L')
                l += 1
            else:
                last = a[r]
                res.append('R')
                r -= 1
            picked = True
            continue

        if last < a[l]:
            last = a[l]
            res.append('L')
            l += 1
            picked = True
            continue

        if last < a[r]:
            last = a[r]
            res.append('R')
            r -= 1
            picked = True
            continue

    print(len(res))
    print("".join(res))


def __starting_point():
    main()


__starting_point()
