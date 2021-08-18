def main():
    A, B, X = list(map(int, input().split()))
    num_max = 10 ** 9

    right = num_max + 1
    ok_max = 0
    cnt = 0
    while right - ok_max > 1:
        mid = (right + ok_max) // 2
        res = A * mid + B * len(str(mid))
        if res <= X:
            ok_max = mid
        else:
            right = mid
        cnt += 1
    print(ok_max)


def __starting_point():
    main()


__starting_point()
