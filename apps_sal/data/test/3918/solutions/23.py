def main():
    n, k1, k2 = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [(abs(a[i] - b[i])) for i in range(n)]
    s = sum(c)
    if s >= (k1 + k2):
        op = (k1 + k2)
        while op > 0:
            c = sorted(c)
            c[-1] -= 1
            op -= 1
        ans = sum([x**2 for x in c])
    else:
        after = (k1 + k2) - s
        if after % 2 == 0:
            ans = 0
        else:
            ans = 1
    print(ans)


def __starting_point():
    main()
__starting_point()
