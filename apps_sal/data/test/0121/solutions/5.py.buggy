n = 4


def check(f):
    nonlocal n
    for i in range(n):
        ok = True
        for j in range(n - 1):
            ok &= f[i][j] == 'x'
        if ok:
            return ok
        ok = True
        for j in range(1, n):
            ok &= f[i][j] == 'x'
        if ok:
            return ok
    for i in range(n):
        ok = True
        for j in range(n - 1):
            ok &= f[j][i] == 'x'
        if ok:
            return ok
        ok = True
        for j in range(1, n):
            ok &= f[j][i] == 'x'
        if ok:
            return ok
    ok = True
    for i in range(n - 1):
        ok &= f[i][i] == 'x'
    if ok:
        return ok
    ok = True
    for i in range(1, n):
        ok &= f[i][i] == 'x'
    if ok:
        return ok
    if f[1][0] == f[2][1] == f[3][2] == 'x' or f[0][1] == f[1][2] == f[2][3] == 'x':
        return True
    return f[3][0] == f[2][1] == f[1][2] == 'x' or f[0][3] == f[2][1] == f[1][2] == 'x' or f[2][0] == f[1][1] == f[0][2] == 'x' or f[1][3] == f[2][2] == f[3][1] == 'x'


f = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(n):
        if f[i][j] == '.':
            f[i][j] = 'x'
            if check(f):
                print("YES")
                return
            f[i][j] = '.'
print("NO")
