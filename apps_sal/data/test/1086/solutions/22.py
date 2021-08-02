import sys
#input = sys.stdin.readline


def main():
    def inp(): return list(map(int, input().split()))
    h, w = inp()
    a = [inp() for _ in range(h)]
    b = [inp() for _ in range(h)]
    d = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            d[i][j] = abs(a[i][j] - b[i][j])
    zero = 80 * (h + w) + 2
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 << (zero + d[0][0]) | 1 << (zero - d[0][0])
    for i in range(h):
        for j in range(w):
            if i == 0:
                if j == 0:
                    continue
                else:
                    dp[i][j] = dp[i][j - 1] << d[i][j] | dp[i][j - 1] >> d[i][j]
            else:
                if j == 0:
                    dp[i][j] = dp[i - 1][j] << d[i][j] | dp[i - 1][j] >> d[i][j]
                else:
                    dp[i][j] = dp[i - 1][j] << d[i][j] | dp[i - 1][j] >> d[i][j]
                    dp[i][j] = dp[i][j] | (dp[i][j - 1] << d[i][j] | dp[i][j - 1] >> d[i][j])
    ans = dp[-1][-1]
    for i in range(zero):
        if ans >> (zero + i) & 1 or ans >> (zero - i) & 1:
            print(i)
            return


def __starting_point():
    main()


__starting_point()
