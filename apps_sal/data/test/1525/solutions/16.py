def main():
    MOD = 10 ** 9 + 7
    (H, W, K) = list(map(int, input().split()))
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for bit in range(1 << W - 1):
            if '11' in bin(bit):
                continue
            toes = list(range(W))
            for j in range(W - 1):
                if bit >> j & 1:
                    (toes[j], toes[j + 1]) = (toes[j + 1], toes[j])
            for (frm, to) in enumerate(toes):
                dp[h + 1][to] = (dp[h + 1][to] + dp[h][frm]) % MOD
    ans = dp[H][K - 1]
    print(ans)


def __starting_point():
    main()


__starting_point()
