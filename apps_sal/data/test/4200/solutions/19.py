def readinput():
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    return (n, m, a)


def main(n, m, a):
    a.sort(reverse=True)
    total = sum(a)
    if a[m - 1] * (4 * m) < total:
        return 'No'
    else:
        return 'Yes'


def __starting_point():
    (n, m, a) = readinput()
    ans = main(n, m, a)
    print(ans)


__starting_point()
