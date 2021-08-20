import sys
input = sys.stdin.readline


def main():
    (h, w) = map(int, input().split())
    red = [[int(x) for x in input().split()] for _ in range(h)]
    blue = [[int(x) for x in input().split()] for _ in range(h)]
    max_dp = 13000
    dp_first = 2 ** max_dp
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(h):
        for j in range(w):
            sub = dp[i][j + 1] | dp[i + 1][j]
            sub = sub | dp_first if i == j == 0 else sub
            shift = abs(red[i][j] - blue[i][j])
            dp[i + 1][j + 1] = sub << shift | sub >> shift
    judge = dp[h][w]
    for i in range(max_dp):
        if judge >> max_dp + i & 1 or judge >> max_dp - i & 1:
            print(i)
            return


def __starting_point():
    main()


__starting_point()
