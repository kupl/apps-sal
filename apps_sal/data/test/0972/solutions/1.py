n, m = map(int, input().split())
z = [[] for i in range(n + 1)]

for i in range(n):
    a = input()
    for j in a:
        z[i].append(j)


def solve(n, m):
    for i in range(n):
        cnt = 0
        for j in range(1, m):
            if z[i][j] != z[i][j - 1]:
                cnt += 1
        if cnt > 2:
            return 1
        if cnt == 2 and z[i][0] == 'B':
            return 1

    for j in range(m):
        cnt = 0
        for i in range(1, n):
            if z[i][j] != z[i - 1][j]:
                cnt += 1
        if cnt > 2:
            return 1
        if cnt == 2 and z[0][j] == 'B':
            return 1
    for i in range(n):
        for j in range(m):
            if z[i][j] == 'B':
                for x in range(i, n):
                    for y in range(m):
                        if z[x][y] == 'B':
                            if z[i][y] == 'W' and z[x][j] == 'W':
                                return 1
    return 0


print(['YES', 'NO'][solve(n, m)])
