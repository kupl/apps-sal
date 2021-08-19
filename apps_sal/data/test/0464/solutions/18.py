(n, m) = list(map(int, input().split()))
seen = [[False] * m for _ in range(n)]
mat = [input() for _ in range(n)]


def is_cross(i, j):
    if i == 0 or i == n - 1 or j == 0 or (j == m - 1) or (mat[i - 1][j] != '*') or (mat[i + 1][j] != '*') or (mat[i][j - 1] != '*') or (mat[i][j + 1] != '*'):
        return (False, None, None)
    else:
        top = i - 1
        bot = i + 1
        left = j - 1
        right = j + 1
        while top > 0 and mat[top - 1][j] == '*':
            top -= 1
        while left > 0 and mat[i][left - 1] == '*':
            left -= 1
        while bot < n - 1 and mat[bot + 1][j] == '*':
            bot += 1
        while right < m - 1 and mat[i][right + 1] == '*':
            right += 1
        return (True, [[top, bot], [left, right]], (i, j))


found = False
for i in range(n):
    for j in range(m):
        if mat[i][j] == '*':
            (is_a_cross, sizes, center) = is_cross(i, j)
            if is_a_cross:
                found = True
                break
    if found:
        break
answered = False
if found:
    (top, bot) = sizes[0]
    (left, right) = sizes[1]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '*':
                if i == center[0]:
                    if j not in list(range(left, right + 1)):
                        print('NO')
                        answered = True
                elif j == center[1]:
                    if i not in list(range(top, bot + 1)):
                        print('NO')
                        answered = True
                else:
                    print('NO')
                    answered = True
            if answered:
                break
        if answered:
            break
    if not answered:
        print('YES')
else:
    print('NO')
