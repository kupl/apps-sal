def main():
    N = int(input())
    TA = [list(map(int, input().split(' '))) for _ in range(N)]
    if N == 1:
        print(sum(TA[0]))
        return
    cur_t, cur_a = TA[0]
    for t, a in TA[1:]:
        ratio = max([(cur_t + t - 1) // t, (cur_a + a - 1) // a])
        cur_t, cur_a = ratio * t, ratio * a
    print(cur_t + cur_a)


def __starting_point():
    main()
__starting_point()
