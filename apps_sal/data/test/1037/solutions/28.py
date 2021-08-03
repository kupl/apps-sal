#!python3

def iim(): return list(map(int, input().rstrip().split()))


def resolve():
    N = int(input())
    A = list(enumerate(iim()))

    A.sort(key=lambda x: (x[1], (2 * x[0] - N)**2), reverse=True)

    dp = [0] * (N + 1)
    dp0 = dp[:]
    for i, (j, ai) in enumerate(A):
        for k in range(i + 1):
            dp[k] = max(dp[k], dp0[k] + abs(N - i + k - 1 - j) * ai)
            dp[k + 1] = max(dp[k + 1], dp0[k] + abs(k - j) * ai)
        dp, dp0 = dp0, dp

    print((max(dp0)))


def __starting_point():
    resolve()


__starting_point()
