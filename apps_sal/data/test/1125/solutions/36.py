import numpy as np


def LI(): return list(map(int, input().split()))


N = int(input())
A = LI()


def main():
    s = 0
    for a in A[2:]:
        s ^= a
    t = A[0] + A[1]
    def f(x): return list(map(int, format(x, "050b")[::-1]))
    sb = f(s)
    tb = f(t)
    ab = f(A[0])

    dp = np.full((51, 2, 2), -1, dtype=int)
    dp[0][0][0] = 0
    for i in range(50):
        for j in range(2):
            for k in range(2):
                if dp[i][j][k] == -1:
                    continue
                for na in range(2):
                    for nb in range(2):
                        if na ^ nb != sb[i] or (na + nb + j) % 2 != tb[i]:
                            continue
                        nj = (na + nb + j) // 2
                        if na == ab[i]:
                            nk = k
                        elif na == 1:
                            nk = 1
                        else:
                            nk = 0
                        v = dp[i][j][k] + (2 ** i) * na
                        dp[i + 1][nj][nk] = max(dp[i + 1][nj][nk], v)

    if dp[-1][0][0] < 1:
        ans = -1
    else:
        ans = A[0] - dp[-1][0][0]
    print(ans)


def __starting_point():
    main()


__starting_point()
