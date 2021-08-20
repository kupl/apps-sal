def main():
    (N, K) = list(map(int, input().split()))
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    XY.sort()
    XY = tuple(XY)

    def count(x_min, x_max, y_min, y_max, i, j):
        OK = 0
        for (m, n) in XY[i:j + 1]:
            if y_min <= n <= y_max:
                OK += 1
        if OK >= K:
            return True
        return False
    ans = 10 ** 20
    for (i, val_i) in enumerate(XY[:N - 1]):
        a = val_i[0]
        for j in range(i + K - 1, N):
            b = XY[j][0]
            e = b - a
            for (k, c) in XY:
                for (l, d) in XY:
                    if c < d:
                        if e * (d - c) < ans and count(a, b, c, d, i, j):
                            ans = e * (d - c)
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
