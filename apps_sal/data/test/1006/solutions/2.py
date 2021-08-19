n = int(input())
m = [list(input()) for i in range(n)]


def test(m, n):
    for r in range(n):
        for c in range(n):
            if m[r][c] == '#':
                if c == 0 or c == n - 1 or r >= n - 2:
                    return False
                elif m[r + 1][c - 1] == '#' and m[r + 1][c] == '#' and (m[r + 1][c + 1] == '#') and (m[r + 2][c] == '#'):
                    m[r + 1][c - 1] = '.'
                    m[r + 1][c] = '.'
                    m[r + 1][c + 1] = '.'
                    m[r + 2][c] = '.'
                else:
                    return False
    return True


print('YES' if test(m, n) else 'NO')
