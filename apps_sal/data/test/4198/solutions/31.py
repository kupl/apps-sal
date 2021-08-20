def main():
    (A, B, X) = list(map(int, input().split()))
    num_max = 10 ** 9
    ok = 0
    ng = num_max + 1
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        res = A * mid + B * len(str(mid))
        if res <= X:
            ok = mid
        else:
            ng = mid
    print(ok)


def __starting_point():
    main()


__starting_point()
