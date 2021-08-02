def main():
    n = int(input())
    A = list(map(int, input().split()))
    x = A[0] ^ A[1]
    for i in A:
        x ^= i
    s = A[0] + A[1]
    dp = [[[-1] * 2 for _ in range(2)] for _ in range(43)]
    dp[0][0][0] = 0
    v = 1
    a = A[0]
    for i in range(42):
        cx, ca, cs = x & 1, a & 1, s & 1
        for j in range(2):
            for k in range(2):
                if dp[i][j][k] == -1:
                    continue
                for na in range(2):
                    for nb in range(2):
                        if na ^ nb != cx:
                            continue
                        ni, nj, nk, ns = i + 1, 0, k, na + nb + j
                        if ns % 2 != cs:
                            continue
                        if ns >= 2:
                            nj = 1
                        if ca < na:
                            nk = 1
                        elif ca == na:
                            nk = k
                        else:
                            nk = 0
                        dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k] | (v * na))
        x >>= 1
        s >>= 1
        a >>= 1
        v <<= 1
    a = dp[42][0][0]
    if a == 0 or a == -1:
        ans = -1
    else:
        ans = A[0] - a
    print(ans)


def __starting_point():
    main()


__starting_point()
