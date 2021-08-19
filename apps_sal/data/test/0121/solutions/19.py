def has_win(mat, r, c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j and i == 0 or not 0 <= i + r < 4 or (not 0 <= j + c < 4):
                continue
            if mat[r + i][c + j] in ['x', '.']:
                tm = '.' if mat[r + i][c + j] == 'x' else 'x'
                if 0 <= r + 2 * i < 4 and 0 <= c + 2 * j < 4 and (mat[r + 2 * i][c + 2 * j] == tm):
                    return True
    return False


def is_win(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 'x' and has_win(mat, i, j):
                return True
    return False


def nput(n):
    for i in range(n):
        yield input()


def main():
    mat = [list(l) for l in nput(4)]
    if is_win(mat):
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
