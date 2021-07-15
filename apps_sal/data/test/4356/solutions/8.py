n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        if b[0][0] == a[i][j]:
            cnt = 0
            for x in range(m):
                flag = True
                if flag == False:
                    break
                for y in range(m):
                    if b[x][y] == a[i+x][j+y]:
                        cnt += 1
                        pass
                    else:
                        flag = False
                        break
                    if cnt == m**2:
                        print("Yes")
                        return
print("No")
