import itertools


def amida_patterns(w):
    ret = list()
    for bars in itertools.product([0, 1], repeat=w - 1):
        if sum([b * bb for (b, bb) in zip(bars[1:], bars[:-1])]) > 0:
            continue
        location = list(range(w))
        for i in range(w):
            if i > 0 and bars[i - 1] == 1:
                location[i] = i - 1
            elif i < w - 1 and bars[i] == 1:
                location[i] = i + 1
        ret.append(location)
    return ret


def main():
    MOD = 10 ** 9 + 7
    (H, W, K) = list(map(int, input().split(' ')))
    ap_list = amida_patterns(W)
    dp = [[0 for _ in range(W)] for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(1, H + 1):
        for a in ap_list:
            for w in range(W):
                dp[h][a[w]] += dp[h - 1][w]
                dp[h][a[w]] %= MOD
    print(dp[H][K - 1])


def __starting_point():
    main()


__starting_point()
