import sys


def comb(n, r, mod=None):
    if r == 0 or r == n:
        return 1
    r = min([r, n - r])
    x, y = 1, 1
    ans = 1
    for i in range(1, r + 1):
        if mod:
            x *= n + 1 - i
            y *= i
            x %= mod
            y %= mod
        else:
            ans *= n + 1 - i
            ans //= i
    ans = x * pow(y, mod - 2, mod) % mod if mod else ans
    return ans


def main():
    h, w, k = map(int, input().split())
    mod = pow(10, 9) + 7

    if w == 1:
        print(1)
        return

    comb_list = [[0] * 11 for _ in range(11)]
    for i in range(11):
        for j in range(11):
            if i >= j:
                comb_list[i][j] = comb(i, j)

    key_list = [1] * 10
    for i in range(1, 10):
        key = 0
        for j in range(1, 10):
            if i < j * 2 - 1:
                break
            key += comb_list[i - j + 1][j]
        key_list[i] += key

    dp = [[0] * w for _ in range(h)]
    for i in range(h):
        if i == 0:
            dp[0][0] = key_list[w - 2]
            dp[0][1] = key_list[w - 3] if w != 2 else 1
            continue
        if w == 2:
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % mod
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % mod
            continue

        for j in range(w):
            if j == 0:
                dp[i][j] = (dp[i - 1][j] * key_list[w - 2] + dp[i - 1][j + 1] * key_list[w - 3]) % mod
            elif j == w - 1:
                dp[i][j] = (dp[i - 1][j] * key_list[w - 2] + dp[i - 1][j - 1] * key_list[w - 3]) % mod
            else:
                dp[i][j] = 0
                dp[i][j] += (dp[i - 1][j - 1] * key_list[max([0, j - 2])] * key_list[max([0, w - 2 - j])]) % mod
                dp[i][j] += (dp[i - 1][j] * key_list[max([0, j - 1])] * key_list[max([0, w - 2 - j])]) % mod
                dp[i][j] += (dp[i - 1][j + 1] * key_list[max([0, j - 1])] * key_list[max([0, w - 3 - j])]) % mod
                dp[i][j] %= mod
    print(dp[h - 1][k - 1])


def __starting_point():
    main()


__starting_point()
