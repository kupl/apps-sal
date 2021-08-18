3


def check_l(a, l, r):
    d = 0
    last = 0
    while l <= r and a[l] > last:
        last = a[l]
        l += 1
        d += 1
    return d


def check_r(a, l, r):
    d = 0
    last = 0
    while l <= r and a[r] > last:
        last = a[r]
        r -= 1
        d += 1
    return d


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
            elif a[l] == a[r]:
                dl = check_l(a, l, r)
                dr = check_r(a, l, r)

                if dl > dr:
                    res.extend(['L'] * dl)
                    last = a[l + dl - 1]
                    l += dl
                else:
                    res.extend(['R'] * dr)
                    last = a[r - dr + 1]
                    r -= dr
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
