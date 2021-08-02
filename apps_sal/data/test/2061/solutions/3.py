def ex(i, j, n, m):
    if i < n and i >= 0 and j < m and j >= 0:
        return True
    else:
        return False


n, m, k = map(int, input().split())
A = []
for i in range(n):
    A.append(list(input()))
B = [[False for i in range(m)] for j in range(n)]
L = []
for i in range(n):
    for j in range(m):
        if not B[i][j] and A[i][j] == '.':
            sides = False
            Oz = [[i, j]]
            count = 1
            Q = [[i, j]]
            B[i][j] = True
            while len(Q) > 0:
                x, y = Q[0][0], Q[0][1]
                if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                    sides = True
                if ex(x - 1, y, n, m) and not B[x - 1][y] and A[x - 1][y] == '.':
                    Q.append([x - 1, y])
                    B[x - 1][y] = True
                    count += 1
                    Oz.append([x - 1, y])
                if ex(x + 1, y, n, m) and not B[x + 1][y] and A[x + 1][y] == '.':
                    Q.append([x + 1, y])
                    B[x + 1][y] = True
                    count += 1
                    Oz.append([x + 1, y])
                if ex(x, y - 1, n, m) and not B[x][y - 1] and A[x][y - 1] == '.':
                    Q.append([x, y - 1])
                    B[x][y - 1] = True
                    count += 1
                    Oz.append([x, y - 1])
                if ex(x, y + 1, n, m) and not B[x][y + 1] and A[x][y + 1] == '.':
                    Q.append([x, y + 1])
                    B[x][y + 1] = True
                    count += 1
                    Oz.append([x, y + 1])
                Q.pop(0)
            if not sides:
                L.append([count, Oz])
L.sort()
s = len(L)
ans = 0
for i in range(s - k):
    ans += L[i][0]
    for j in L[i][1]:
        A[j[0]][j[1]] = '*'
print(ans)
for i in range(n):
    for j in range(m):
        print(A[i][j], end='')
    print()
