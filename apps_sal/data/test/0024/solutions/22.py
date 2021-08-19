def check(a, b):
    if m[a][b] != '.':
        return False
    else:
        cnt = 0
        p = a + 1
        while p < 10 and m[p][b] == 'X':
            p += 1
            cnt += 1
        p = a - 1
        while p >= 0 and m[p][b] == 'X':
            p -= 1
            cnt += 1
        if cnt >= 4:
            return True
        cnt = 0
        p = b + 1
        while p < 10 and m[a][p] == 'X':
            p += 1
            cnt += 1
        p = b - 1
        while p >= 0 and m[a][p] == 'X':
            p -= 1
            cnt += 1
        if cnt >= 4:
            return True
        cnt = 0
        p = 1
        while a + p < 10 and b + p < 10 and (m[a + p][b + p] == 'X'):
            p += 1
            cnt += 1
        p = -1
        while a + p >= 0 and b + p >= 0 and (m[a + p][b + p] == 'X'):
            p -= 1
            cnt += 1
        if cnt >= 4:
            return True
        cnt = 0
        p = 1
        while a + p < 10 and b - p >= 0 and (m[a + p][b - p] == 'X'):
            p += 1
            cnt += 1
        p = -1
        while a + p >= 0 and b - p < 10 and (m[a + p][b - p] == 'X'):
            p -= 1
            cnt += 1
        if cnt >= 4:
            return True
    return False


m = []
for i in range(10):
    m.append(input())
F = False
for i in range(10):
    for j in range(10):
        if check(i, j):
            F = True
if F:
    print('YES')
else:
    print('NO')
