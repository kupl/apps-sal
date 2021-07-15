M = 1000000007


def main():
    n, k = list(map(int, input().split()))

    f = [1]
    g = [1]
    for i in range(1, 2 * n + 1):
        f.append(i * f[i - 1] % M)
        g.append(pow(f[i], -1, M))
    for i in range(1, k + 1):
        if n - k < i - 1:
            print((0))
        else:
            blue_ball = k - i
            blue_box = i
            blue_comb = f[blue_ball + blue_box - 1] * \
                g[blue_ball] % M * g[blue_box - 1] % M
            red_ball = n - k - i + 1
            red_box = i + 1
            red_comb = f[red_ball + red_box - 1] * \
                g[red_ball] % M * g[red_box - 1] % M
            print((blue_comb * red_comb % M))


def __starting_point():
    main()

__starting_point()
