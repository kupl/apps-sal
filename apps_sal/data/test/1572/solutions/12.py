__author__ = 'Lipen'


def actions(n, a):
    lmax = 2
    if n <= 2:
        return n
    i = 0
    l = 2
    while i < n - 2:
        q = a[i]
        w = a[i + 1]
        x = a[i + 2]
        if x == q + w:
            l += 1
        else:
            if l > lmax:
                lmax = l
            l = 2
        i += 1
    if l > lmax:
        lmax = l
    return lmax


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(actions(n, a))


def __starting_point():
    main()


__starting_point()
