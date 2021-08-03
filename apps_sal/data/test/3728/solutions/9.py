

def judge():
    n, m = list(map(int, input().split()))
    num = [list(map(int, input().split())) for x in range(n)]
    for i in range(m):
        for j in range(m):
            tmp = num[:]
            for k in range(n):
                tmp[k][i], tmp[k][j] = tmp[k][j], tmp[k][i]
            cur = True
            for k in range(n):
                cnt = len([l for l in range(m) if tmp[k][l] != l + 1])
                if cnt > 2:
                    cur = False
            for k in range(n):
                tmp[k][i], tmp[k][j] = tmp[k][j], tmp[k][i]
            if cur:
                return True
    return False


if judge():
    print('YES')
else:
    print('NO')
