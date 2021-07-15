n = int(input())
a = [list(map(int, input().split())) for i in range(2)]
if n != 1:
    sum_up, pref_up, sum_down, pref_down = [[[0 for i in range(n)] for j in range(2)] for _ in range(4)]
    for i in range(2):
        sum_up[i][n - 1] = a[i][n - 1]
        pref_up[i][n - 1] = a[i][n - 1]
        pref_down[i][n - 1] = a[i][n - 1]
        for j in range(n - 2, -1, -1):
            sum_up[i][j] = sum_up[i][j + 1] + a[i][j]
            pref_up[i][j] = pref_up[i][j + 1] + sum_up[i][j]
            pref_down[i][j] = pref_down[i][j + 1] + a[i][j] * (n - j)
    zig = [[0 for i in range(n)] for j in range(2)]
    for j in range(n):
        for i in range(2):
            if j % 2 == 0:
                if i == 0:
                    zig[i][j] = a[i][j] * j * 2 + zig[i][j - 1]
                else:
                    zig[i][j] = a[i][j] * (j * 2 + 1) + zig[1 - i][j]
            else:
                if i == 0:
                    zig[1 - i][j] = a[1 - i][j] * j * 2 + zig[1 - i][j - 1]
                else:
                    zig[1 - i][j] = a[1 - i][j] * (j * 2 + 1) + zig[i][j]
    ans = -1e18
    for j in range(n):
        if j == 0:
            ans = max(ans, pref_up[0][j] + pref_down[1][j] + sum_up[1][j] * n - sum_up[0][j] - sum_up[1][j])
        else:
            if j == n - 1:
                ans = max(ans, zig[1 - (j % 2)][n - 1])
            else:
                if j % 2 == 1:
                    ans = max(ans, pref_up[0][j + 1] + sum_up[0][j + 1] * (4 * (j // 2 + 1) - 1) + pref_down[1][j + 1] - sum_up[1][j + 1] + sum_up[1][j + 1] * (4 * (j // 2 + 1) - 1 + n - j) + zig[0][j])
                else:
                    ans = max(ans, pref_up[1][j + 1] - sum_up[1][j + 1] + sum_up[1][j + 1] * (4 * (j // 2) + 2) +
                              pref_down[0][j + 1] - sum_up[0][j + 1] + sum_up[0][j + 1] * (
                                          4 * (j // 2) + 2 - 1 + n - j) + zig[1][j])
    ans = max(ans, pref_up[1][0] + pref_down[0][1] + sum_up[0][1] * n)
    print(ans)
else:
    print(a[1][0])

