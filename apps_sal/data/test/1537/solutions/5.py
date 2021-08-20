def main():
    (n, k) = list(map(int, input().split()))
    ss = []
    tate = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    yoko = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        s = input().strip()
        for (j, _s) in enumerate(s):
            tate[i + 1][j + 1] = tate[i][j + 1] + (1 if _s == 'B' else 0)
            yoko[i + 1][j + 1] = yoko[i + 1][j] + (1 if _s == 'B' else 0)
    lc = 0
    for i in range(n):
        if tate[n][i + 1] == 0:
            lc += 1
        if yoko[i + 1][n] == 0:
            lc += 1
    yans = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    tans = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        (l, r) = (0, k)
        while r <= n:
            yans[i + 1][l + 1] = yans[i][l + 1]
            if yoko[i + 1][n] != 0 and yoko[i + 1][r] - yoko[i + 1][l] == yoko[i + 1][n]:
                yans[i + 1][l + 1] += 1
            l += 1
            r += 1
    for i in range(n):
        (l, r) = (0, k)
        while r <= n:
            tans[l + 1][i + 1] = tans[l + 1][i]
            if tate[n][i + 1] != 0 and tate[r][i + 1] - tate[l][i + 1] == tate[n][i + 1]:
                tans[l + 1][i + 1] += 1
            l += 1
            r += 1
    ans = lc
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            ans = max(ans, lc + yans[i + k][j + 1] - yans[i][j + 1] + tans[i + 1][j + k] - tans[i + 1][j])
    print(ans)


def __starting_point():
    main()


__starting_point()
