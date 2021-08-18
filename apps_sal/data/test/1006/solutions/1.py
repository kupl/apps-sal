def deleteCross(m, i, j):
    if i <= 0 or j <= 0 or i >= len(m) - 1 or j >= len(m) - 1:
        return (m, False)
    if m[i][j] == r'
      m[i][j] = m[i + 1][j] = m[i - 1][j] = m[i][j + 1] = m[i][j - 1] = '.'
       return (m, True)
    return (m, False)


def solve(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == r'
              r1 = deleteCross(m, i + 1, j)
               if not r1[1]:
                    return False
                m = r1[0]
    return True


n = int(input())
m = []
for i in range(n):
    m.append(list(input()))
print('YES' if solve(m) else 'NO')
