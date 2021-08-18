def modify_seq(seq: list, is_positive: bool) -> int:
    cur, cnt = 0, 0
    for i in seq:
        cur += i
        if is_positive and cur <= 0:
            cnt += abs(cur) + 1
            cur = 1
        elif not is_positive and cur >= 0:
            cnt += abs(cur) + 1
            cur = -1
        is_positive = not is_positive
    return cnt


def main():
    _, *A = list(map(int, open(0).read().split()))
    print((min(modify_seq(A, True), modify_seq(A, False))))


def __starting_point():
    main()


__starting_point()
