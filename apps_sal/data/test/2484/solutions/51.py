import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    csum = [[0] * 20 for _ in range(N + 1)]
    for i in range(N):
        for j in range(20):
            csum[i + 1][j] = csum[i][j] + (1 if A[i] & (1 << j) else 0)

    def is_ok(l, r):
        res = True
        for j in range(20):
            if csum[r][j] - csum[l][j] > 1:
                res = False
                break
        return res

    ans = 0
    right = 0
    for left in range(N):
        while right < N and is_ok(left, right + 1):
            right += 1

        ans += right - left

        if left == right:
            right += 1

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
