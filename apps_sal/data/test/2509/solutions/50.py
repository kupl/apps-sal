from sys import stdin


def main():
    # 入力
    readline = stdin.readline
    n, k = map(int, readline().split())

    if k == 0:
        print(n**2)
    else:
        res = 0
        for b in range(1, n + 1):
            if b <= k:
                continue
            else:
                m = n // b
                l = n % b
                res += (b - k) * m
                res += max(0, l - k + 1)

        print(res)


def __starting_point():
    main()


__starting_point()
