def main():
    (n, M) = [int(i) for i in input().split(' ')]
    a = [0] + [int(i) for i in input().split(' ')] + [M]
    n = n + 2
    incr_sum = []
    s = 0
    for i in range(n):
        if i % 2 == 1:
            s += a[i] - a[i - 1]
        incr_sum.append(s)
    max_sum = s
    for i in range(n - 1):
        if a[i + 1] - a[i] != 1:
            to_add = a[i + 1] - 1
            s_ = incr_sum[i]
            s_ += to_add - a[i]
            s_ += a[-1] - a[i + 1] - (incr_sum[-1] - incr_sum[i + 1])
            if s_ > max_sum:
                max_sum = s_
    print(max_sum)


def __starting_point():
    main()


__starting_point()
