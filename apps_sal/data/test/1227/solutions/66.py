
def resolve():
    S = input()
    K = int(input())
    N = len(S)

    dp = [[[0] * 2 for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(4):
            for smaller in range(2):
                now = int(S[i])
                for d in range(10):
                    ni = i + 1
                    nj = j
                    n_smaller = smaller
                    if d != 0:
                        nj += 1
                    if nj > K:
                        continue
                    if smaller == 0:
                        if d > now:
                            continue
                        if d < now:
                            n_smaller = 1
                    dp[ni][nj][n_smaller] += dp[i][j][smaller]
    ans = dp[N][K][0] + dp[N][K][1]
    print(ans)


def __starting_point():
    resolve()


__starting_point()
