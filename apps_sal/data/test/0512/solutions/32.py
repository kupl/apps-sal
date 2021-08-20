import sys


def main():
    sys.setrecursionlimit(10 ** 7)

    def LI():
        return [int(x) for x in sys.stdin.readline().split()]

    def NI():
        return int(sys.stdin.readline())
    N = NI()
    c = [0] * (2 * N + 1)
    f = [0] * (2 * N + 1)
    for _ in range(N):
        (a, b) = LI()
        if a > 0:
            if c[a] != 0 or f[a] != 0:
                print('No')
                return
            c[a] = b
        if b > 0:
            if c[b] != 0 or f[b] != 0:
                print('No')
                return
            f[b] = a
        if a >= b and a > 0 and (b > 0):
            print('No')
            return
    dp = [[-1] * (2 * N + 1) for _ in range(2 * N + 1)]

    def check(i, j):
        if dp[i][j] >= 0:
            return bool(dp[i][j])
        for k in range(i, j + 1):
            if c[k] != 0:
                if k > (i + j) // 2:
                    break
                if c[k] > 0 and c[k] - k != (j - i + 1) // 2:
                    break
                if c[k] < 0 and f[k + (j - i + 1) // 2] != 0:
                    break
            if f[k] != 0:
                if k <= (i + j) // 2:
                    break
                if f[k] > 0 and k - f[k] != (j - i + 1) // 2:
                    break
                if f[k] < 0 and c[k - (j - i + 1) // 2] != 0:
                    break
        else:
            dp[i][j] = 1
            return bool(dp[i][j])
        for k in range(i + 2, j, 2):
            ret1 = check(i, k - 1)
            ret2 = check(k, j)
            if ret1 and ret2:
                dp[i][j] = 1
                return bool(dp[i][j])
        dp[i][j] = 0
        return bool(dp[i][j])
    if check(1, 2 * N):
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
