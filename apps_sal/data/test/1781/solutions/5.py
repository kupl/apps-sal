def insertp():
    x, y = 0, 0
    min = 3
    for i in range(n):
        for j in range(12):
            if a[i][j] == '.':
                if j != 0 and j != 11:
                    if a[i][j - 1] != 'S':
                        if a[i][j + 1] != 'S':
                            a[i][j] = 'x'
                            return 0
                        else:
                            if min > 1:
                                min = 1
                                x, y = i, j
                    else:
                        if a[i][j + 1] != 'S':
                            if min > 1:
                                min = 1
                                x, y = i, j
                        else:
                            if min > 2:
                                min = 2
                                x, y = i, j
                elif j == 0:
                    if a[i][j + 1] != 'S':
                        a[i][j] = 'x'
                        return 0
                    else:
                        if min > 1:
                            min = 1
                            x, y = i, j
                else:
                    if a[i][j - 1] != 'S':
                        a[i][j] = 'x'
                        return 0
                    else:
                        if min > 1:
                            min = 1
                            x, y = i, j
    a[x][y] = 'x'
    return min


n, k = map(int, input().split())
a = [list(input()) for i in range(n)]
ans = 0

for i in range(n):
    for j in range(12):
        if a[i][j] == 'S':
            if j != 0 and j != 11:
                if a[i][j - 1] == 'P' or a[i][j - 1] == 'S':
                    ans += 1
                if a[i][j + 1] == 'P' or a[i][j + 1] == 'S':
                    ans += 1
            elif j == 0:
                if a[i][j + 1] == 'P' or a[i][j + 1] == 'S':
                    ans += 1
            else:
                if a[i][j - 1] == 'P' or a[i][j - 1] == 'S':
                    ans += 1

for i in range(k):
    ans += insertp()

print(ans)
for i in range(n):
    for j in range(12):
        print(a[i][j], end='')
    print()
