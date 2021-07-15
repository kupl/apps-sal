n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

success = 0
for i in range(n - m + 1):
    fail = 0
    for j in range(n - m + 1):
        fail = 0
        for ii in range(m):
            for jj in range(m):
                if b[ii][jj] == a[i + ii][j + jj]:
                    continue
                else:
                    fail = 1
                    break
            if fail == 1:
                break
        else:
            success = 1
            print('Yes')
            break
    if success == 1:
        break
else:
    if fail == 1:
        print('No')
