n = 0
k = 0
mat = []


def check(i, j):
    ver_count = 1
    hor_count = 1
    dial1_count = 1
    dial2_count = 1

    ti = i - 1
    tj = j
    while ti >= 0 and mat[ti][j] == 'X':
        ver_count += 1
        ti -= 1
    ti = i + 1
    while ti < n and mat[ti][j] == 'X':
        ver_count += 1
        ti += 1
    ti = i
    tj = j - 1
    while tj >= 0 and mat[i][tj] == 'X':
        hor_count += 1
        tj -= 1
    tj = j + 1
    while tj < n and mat[i][tj] == 'X':
        hor_count += 1
        tj += 1
    ti = i - 1
    tj = j - 1
    while ti >= 0 and tj >= 0 and mat[ti][tj] == 'X':
        dial1_count += 1
        ti -= 1
        tj -= 1
    ti = i + 1
    tj = j + 1
    while ti < n and tj < n and mat[ti][tj] == 'X':
        dial1_count += 1
        ti += 1
        tj += 1
    ti = i - 1
    tj = j + 1
    while ti >= 0 and tj < n and mat[ti][tj] == 'X':
        dial2_count += 1
        ti -= 1
        tj += 1
    ti = i + 1
    tj = j - 1
    while ti < n and tj >= 0 and mat[ti][tj] == 'X':
        dial2_count += 1
        ti += 1
        tj -= 1
    if ver_count >= k or hor_count >= k or dial1_count >= k or dial2_count >= k:
        return True
    else:
        return False


t = eval(input())
while t > 0:
    n, k = list(map(int, input().split()))
    tn = n
    mat = []
    while tn > 0:
        mat.append(input().strip())
        tn -= 1
    canWin = False
    i = 0
    for row in mat:
        j = 0
        for cell in row:
            if cell == '.' and check(i, j):
                canWin = True
                break
            j += 1
        i += 1
    if canWin:
        print('YES')
    else:
        print('NO')
    t -= 1
