(n, m) = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))


def result(a, n, m):
    r = 0
    for i in range(-1, -m, -1):
        if a[-1][i] == 0:
            a[-1][i] = a[-1][i + 1] - 1
        if a[-1][i] <= a[-1][i - 1] or a[-1][i] <= a[-2][i]:
            return -1
        r = r + a[-1][i]
    if a[-1][-m] == 0:
        a[-1][-m] = a[-1][-m + 1] - 1
    if a[-1][-m] <= a[-2][-m]:
        return -1
    r = r + a[-1][-m]
    for i in range(-2, -n, -1):
        for j in range(-1, -m, -1):
            if j == -1:
                if a[i][j] == 0:
                    a[i][j] == a[i + 1][j] - 1
                if a[i][j] <= a[i][j - 1] or a[i][j] <= a[i - 1][j]:
                    return -1
                r = r + a[i][j]
                continue
            if a[i][j] == 0:
                a[i][j] = min(a[i + 1][j] - 1, a[i][j + 1] - 1)
            if a[i][j] <= a[i - 1][j] or a[i][j] <= a[i][j - 1]:
                return -1
            r = r + a[i][j]
        if a[i][-m] == 0:
            a[i][-m] = min(a[i + 1][-m] - 1, a[i][-m + 1] - 1)
        if a[i][-m] <= a[i - 1][-m]:
            return -1
        r = r + a[i][-m]
    if a[0][-1] == 0:
        a[0][-1] = a[1][-1] - 1
    if a[0][-1] <= a[0][-2]:
        return -1
    r = r + a[0][-1]
    for i in range(-2, -m, -1):
        if a[0][i] == 0:
            a[0][i] = min(a[0][i + 1] - 1, a[1][i] - 1)
        if a[0][i] <= a[0][i - 1]:
            return -1
        r = r + a[0][i]
    if a[0][0] == 0:
        a[0][0] = min(a[0][1] - 1, a[1][0] - 1)
    r = r + a[0][0]
    return r


print(result(a, n, m))
