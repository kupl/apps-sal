def adjust(x, limit):
    if x == 0:
        return 0

    if x <= limit:
        return x - 1

    return limit


def __starting_point():

    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: -x)
    # print(a)

    for i in range(1, n):
        a[i] = adjust(a[i - 1], a[i])

    print(sum(a))


__starting_point()
