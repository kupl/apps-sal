def main():
    (n, k, p, x, y) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    median = int((n + 1) / 2)
    less = 0
    for i in range(len(a)):
        if a[i] < y:
            less += 1
    if less >= median:
        print(-1)
        return
    fillOne = min(median - less - 1, n - k)
    if sum(a) + fillOne * 1 + (n - k - fillOne) * y > x:
        print(-1)
        return
    for i in range(fillOne):
        print(1, end=' ')
    for i in range(n - k - fillOne):
        print(y, end=' ')


def __starting_point():
    main()


__starting_point()
