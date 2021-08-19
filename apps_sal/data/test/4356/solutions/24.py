def f():
    (n, m) = map(int, input().split())
    a = [list(input()) for i in range(n)]
    b = [list(input()) for j in range(m)]
    for p in range(n - m + 1):
        for q in range(n - m + 1):
            cnt = 0
            for x in range(m):
                for y in range(m):
                    if a[x + p][y + q] == b[x][y]:
                        cnt += 1
                        if cnt == m * m:
                            return 'Yes'
                    else:
                        break
    return 'No'


print(f())
