def main():
    (n, k) = list(map(int, input().split()))
    ruiseki = [0] * (n + 1)
    mod = 998244353
    move_list = [list(map(int, input().split())) for i in range(k)]
    sorted_list = sorted(move_list)
    dp = [0] * (n + 1)
    dp[1] = 1
    ruiseki[1] = 1
    for i in range(2, n + 1):
        for rng in sorted_list:
            left = max(0, i - rng[1] - 1)
            right = min(i - rng[0], i - 1)
            if left < right:
                dp[i] += ruiseki[right] - ruiseki[left]
            else:
                break
        ruiseki[i] = ruiseki[i - 1] % mod + dp[i] % mod
    print(dp[-1] % mod)


def __starting_point():
    main()


__starting_point()
