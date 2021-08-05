def main():
    n, c = map(int, input().split())
    xv = [list(map(int, input().split())) for _ in range(n)]
    v, left_max, right_max = 0, 0, 0
    gl = [None] * n
    gr = [None] * n
    _2oas = [None] * (n + 1)
    _2obs = [None] * (n + 1)
    _2oas[0], _2obs[0] = 0, 0
    ans = 0
    for i, (xi, vi) in enumerate(xv, 1):
        v += vi
        left = v - xi
        if left_max < left:
            left_max = left
        gl[n - i] = left_max
        _2oas[i] = v - 2 * xi
    v = 0
    for i, (xi, vi) in enumerate(xv[::-1], 1):
        v += vi
        right = v - c + xi
        if right_max < right:
            right_max = right
        gr[n - i] = right_max
        _2obs[i] = v - 2 * (c - xi)
    for oa, _2ob, ob, _2oa in zip(gl, _2obs[:n], gr, _2oas[:n]):
        ans = max(ans, _2oa + ob, _2ob + oa)
    print(ans)


def __starting_point():
    main()


__starting_point()
