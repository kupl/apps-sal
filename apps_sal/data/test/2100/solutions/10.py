def main():
    n = int(input())
    ll = rr = 0
    for _ in range(n):
        l, r = list(map(int, (input().split())))
        ll += l
        rr += r
    print(sum(min(_, n - _) for _ in (ll, rr)))


def __starting_point():
    main()


__starting_point()
