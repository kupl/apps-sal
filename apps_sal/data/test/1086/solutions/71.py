import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    (h, w) = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(h)]
    B = [list(map(int, input().split())) for i in range(h)]
    abss = [[abs(A[i][j] - B[i][j]) for j in range(w)] for i in range(h)]
    dp = [[0] * w for i in range(h)]
    dp[0][0] = 1 << abss[0][0] + 13000
    for i in range(h):
        for j in range(w):
            if i != h - 1:
                dp[i + 1][j] = dp[i + 1][j] | dp[i][j] << abss[i + 1][j] | dp[i][j] >> abss[i + 1][j]
            if j != w - 1:
                dp[i][j + 1] = dp[i][j + 1] | dp[i][j] << abss[i][j + 1] | dp[i][j] >> abss[i][j + 1]
    a = 0
    ans = dp[-1][-1]
    while True:
        if ans & 1 << 13000 - a:
            print(a)
            break
        elif ans & 1 << 13000 + a:
            print(a)
            break
        a += 1


def __starting_point():
    main()


__starting_point()
