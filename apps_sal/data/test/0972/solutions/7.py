n, m = list(map(int, input().split()))
c = [input() for _ in ' ' * n]
def sol(n, m):
    for i in range(n):
        count = 0
        for j in range(1, m):
            if c[i][j] != c[i][j - 1]:
                count += 1
        if count > 2:
            return False
        if count == 2 and c[i][0]=='B':
            return False

    for j in range(m):
        count = 0
        for i in range(1, n):
            if c[i][j] != c[i - 1][j]:
                count += 1
        if count > 2:
            return False
        if count == 2 and c[0][j]=='B':
            return False

    for i in range(n):
        for j in range(m):
            if c[i][j] == 'B':
                for x in range(i, n):
                    for y in range(m):
                        if c[x][y] == 'B':
                            if c[i][y] == 'W' and c[x][j] == 'W':
                                return False
    return True


print('NYOE S'[sol(n, m)::2])

