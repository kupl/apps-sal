def solve(H, W, K):
    mod = 10 ** 9 + 7
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if dp[h][w] == 0:
                continue
            for i in range(3):
                new_w = w - 1 + i
                if not 0 <= new_w < W:
                    continue

                def cnt_tmp(n, r, l, flg):
                    re = 0
                    if n >= W - 2:
                        if r <= n <= l:
                            return 1
                        if flg:
                            return 1
                        else:
                            return 2
                    if r <= n <= l:
                        return cnt_tmp(n + 1, r, l, False)
                    re += cnt_tmp(n + 1, r, l, False)
                    re += cnt_tmp(n + 1, r, l, True) if not flg else 0
                    return re
                tmp = cnt_tmp(0, min(w, new_w) - 1, max(w, new_w), False)
                dp[h + 1][new_w] += dp[h][w] * tmp
                dp[h + 1][new_w] %= mod
    print(dp[-1][K - 1])


def __starting_point():
    (H, W, K) = list(map(int, input().split()))
    solve(H, W, K)


__starting_point()
