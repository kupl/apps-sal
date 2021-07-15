n, m = input().split()
n = int(n)
m = int(m)
lst = [[0]*m for i in range(n)]
rec = [[0]*m for i in range(n)]
fin = [[0]*m for i in range(n)]
ans = 0
cnt = 0
for i in range(n):
    tmp = input()
    for j, x in enumerate(tmp):
        if x == '*':
            lst[i][j] = 1
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1 and i > 0 and j > 0 and i < n-1 and j < m-1:
            tmp = min(i, j, n-1-i, m-1-j)
            for k in range(tmp, 0, -1):
                flag = True
                for x in range(1, k+1):
                    if lst[i][j-x] == 0 or lst[i][j+x] == 0 or lst[i-x][j] == 0 or lst[i+x][j] == 0:
                        flag = False
                if flag:
                    fin[i][j] = k
                    break
for i in range(n):
    for j in range(m):
        if fin[i][j] > 0:
            tmp = fin[i][j]
            ans += 1
            cnt += 1 + tmp * 4
            rec[i][j] = 1
            for x in range(tmp+1):
                rec[i][j+x] = 1
                rec[i][j-x] = 1
                rec[i-x][j] = 1
                rec[i+x][j] = 1
if rec != lst:
    print(-1)
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if fin[i][j] > 0:
                print(i+1, j+1, fin[i][j])

