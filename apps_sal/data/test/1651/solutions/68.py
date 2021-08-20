def __starting_point():
    (s, p) = list(map(int, input().split()))
    x = s * s - 4 * p
    x_ = int(x ** 0.5)
    if x_ * x_ != x:
        print('No')
    else:
        x = int(s + x_) / 2
        print('Yes' if x * (s - x) == p else 'No')


__starting_point()
