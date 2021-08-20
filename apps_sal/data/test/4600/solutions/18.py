from collections import defaultdict


def main():
    (n, m) = map(int, input().split(' '))
    d = defaultdict(lambda: '')
    dp = defaultdict(lambda: 0)
    cnt_p = 0
    cnt_ca = 0
    for i in range(m):
        (p, s) = input().split(' ')
        if d[p] == '':
            if s == 'AC':
                d[p] = 1
                cnt_ca += 1
                cnt_p += dp[p]
            else:
                dp[p] += 1
    print(f'{cnt_ca} {cnt_p}')


def __starting_point():
    main()


__starting_point()
