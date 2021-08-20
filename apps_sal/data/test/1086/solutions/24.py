def main():
    (h, w) = list(map(int, input().split()))
    L = 80 * (h + w) + 1
    a = [list(map(int, input().split())) for i in range(h)]
    b = [list(map(int, input().split())) for i in range(h)]
    x = [[abs(a[i][j] - b[i][j]) for j in range(w)] for i in range(h)]
    L = 12800
    state = [[0] * w for _ in range(h)]
    delta = x[0][0]
    state[0][0] = 2 ** L >> delta | 2 ** L << delta
    for j in range(1, w):
        delta = x[0][j]
        state[0][j] = state[0][j - 1] >> delta | state[0][j - 1] << delta
    for i in range(1, h):
        delta = x[i][0]
        state[i][0] = state[i - 1][0] >> delta | state[i - 1][0] << delta
    for i in range(1, h):
        for j in range(1, w):
            delta = x[i][j]
            state[i][j] = state[i][j - 1] >> delta | state[i][j - 1] << delta
            state[i][j] |= state[i - 1][j] >> delta | state[i - 1][j] << delta
    ans = 10 ** 9
    for i in range(L * 2):
        if state[h - 1][w - 1] & 1:
            ans = min(ans, abs(i - L))
        state[h - 1][w - 1] >>= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
