def main():
    MOD = 10**9 + 7
    N, M = list(map(int, input().split(' ')))
    X = list(map(int, input().split(' ')))
    Y = list(map(int, input().split(' ')))
    X.sort()
    Y.sort()
    heights = [Y[i + 1] - Y[i] for i in range(M - 1)]
    widths = [X[j + 1] - X[j] for j in range(N - 1)]
    # first row
    row_areas = [0 for _ in range(M - 1)]
    first_row_area, norm_first_row_area = 0, 0
    for j, w in enumerate(widths):
        first_row_area += (1 + 0) * (M - 0 - 1) * (j + 1) * (N - j - 1) * w * heights[0]
        first_row_area %= MOD
        norm_first_row_area += (j + 1) * (N - j - 1) * w
        norm_first_row_area %= MOD
    row_areas[0] = first_row_area
    # rest rows
    for i in range(1, M - 1):
        area = (i + 1) * (M - i - 1) * norm_first_row_area * heights[i]
        area %= MOD
        row_areas[i] = area
    # answer
    ans = 0
    for a in row_areas:
        ans += a
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
