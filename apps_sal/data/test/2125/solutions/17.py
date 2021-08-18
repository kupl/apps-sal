def test_c(n, m, G):
    mid = [[False for i in range(m)] for j in range(n)]
    vis = [[False for i in range(m)] for j in range(n)]
    L = [[1 for i in range(m)] for j in range(n)]

    for i in range(1, n):
        for j in range(m):
            if G[i][j] != G[i - 1][j]:
                mid[i][j] = True

    for j in range(m):
        for i in range(n):
            if i >= 1 and G[i][j] == G[i - 1][j]:
                L[i][j] = L[i - 1][j] - 1
                continue

            k = 0
            while i + k < n and G[i][j] == G[i + k][j]:
                k += 1
            L[i][j] = k

    cnt = 0
    for i in range(n):
        for j in range(m):
            if mid[i][j] == True and vis[i][j] == False:
                if i - L[i][j] >= 0 and i + L[i][j] < n:
                    if L[i - L[i][j]][j] == L[i][j] and L[i + L[i][j]][j] >= L[i][j]:
                        k = 1
                        vis[i][j] = True
                        while j + k < m and G[i][j] == G[i][j + k] and L[i][j] == L[i][j + k] and mid[i][j + k] == True:
                            if L[i - L[i][j]][j + k] == L[i][j] and G[i - L[i][j]][j + k] == G[i - L[i][j]][j] and\
                               L[i + L[i][j]][j + k] >= L[i][j] and G[i + L[i][j]][j + k] == G[i + L[i][j]][j]:
                                vis[i][j + k] = True
                                k += 1
                            else:
                                break
                        cnt += int(((k + 1) * k) // 2)

    print(cnt)


def __starting_point():

    n, m = [int(x) for x in input().split()]
    G = []
    for i in range(n):
        G.append(list(input()))
    mid = [[False for i in range(m)] for j in range(n)]
    vis = [[False for i in range(m)] for j in range(n)]
    L = [[1 for i in range(m)] for j in range(n)]

    for i in range(1, n):
        for j in range(m):
            if G[i][j] != G[i - 1][j]:
                mid[i][j] = True

    for j in range(m):
        for i in range(n):
            if i >= 1 and G[i][j] == G[i - 1][j]:
                L[i][j] = L[i - 1][j] - 1
                continue

            k = 0
            while i + k < n and G[i][j] == G[i + k][j]:
                k += 1
            L[i][j] = k

    cnt = 0
    for i in range(n):
        for j in range(m):
            if mid[i][j] == True and vis[i][j] == False:
                if i - L[i][j] >= 0 and i + L[i][j] < n:
                    if L[i - L[i][j]][j] == L[i][j] and L[i + L[i][j]][j] >= L[i][j]:
                        k = 1
                        vis[i][j] = True
                        while j + k < m and G[i][j] == G[i][j + k] and L[i][j] == L[i][j + k] and mid[i][j + k] == True:
                            if L[i - L[i][j]][j + k] == L[i][j] and G[i - L[i][j]][j + k] == G[i - L[i][j]][j] and\
                               L[i + L[i][j]][j + k] >= L[i][j] and G[i + L[i][j]][j + k] == G[i + L[i][j]][j]:
                                vis[i][j + k] = True
                                k += 1
                            else:
                                break
                        cnt += int(((k + 1) * k) // 2)

    print(cnt)


__starting_point()
