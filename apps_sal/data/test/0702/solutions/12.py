def solve():
    n = int(input())
    b = [list(input()) for _ in range(n)]
    for i in range(n - 2):
        if b[i][0] == '.' or b[i][-1] == '.':
            return 'NO'
        for j in range(1, n - 1):
            if b[i][j] == '.':
                chg = [(i + 1, j), (i + 2, j), (i + 1, j - 1), (i + 1, j + 1)]
                for (x, y) in chg:
                    if b[x][y] == '#':
                        return 'NO'
                    b[x][y] = '#'
    for i in range(n - 2, n):
        for j in range(n):
            if b[i][j] == '.':
                return 'NO'
    return 'YES'


print(solve())
