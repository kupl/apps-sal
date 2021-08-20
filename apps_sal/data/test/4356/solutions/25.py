def solve(n, m, original, temp):

    def judge(sy, sx):
        for i in range(m):
            for j in range(m):
                if original[sy + i][sx + j] != temp[i][j]:
                    return False
        return True
    sy = 0
    while sy + m - 1 < n:
        sx = 0
        while sx + m - 1 < n:
            if judge(sy, sx):
                return True
            sx += 1
        sy += 1
    return False


def main():
    (N, M) = list(map(int, input().split()))
    a = [input() for _ in range(N)]
    b = [input() for _ in range(M)]
    print('Yes' if solve(N, M, a, b) else 'No')
    return


def __starting_point():
    main()


__starting_point()
