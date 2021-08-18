from collections import deque

T = int(input())


class Found(Exception):
    pass


def neighbours(M, i, j):
    res = []
    if i > 0:
        res.append((i - 1, j))
    if j > 0:
        res.append((i, j - 1))
    if i + 1 < len(M):
        res.append((i + 1, j))
    if j + 1 < len(M[0]):
        res.append((i, j + 1))
    return res


def bfs(M, i, j):
    visited = [[False] * len(M[0]) for _ in range(len(M))]
    visited[i][j] = True
    Q = deque()
    Q.append((i, j))
    answer = 0
    if M[i][j] == 'G':
        answer += 1

    while Q:
        eli, elj = Q.popleft()
        if M[eli][elj] == '
        continue
        for ni, nj in neighbours(M, eli, elj):
            if M[ni][nj] == '
            continue
            if visited[ni][nj]:
                continue
            visited[ni][nj] = True
            Q.append((ni, nj))
            if M[ni][nj] == 'G':
                answer += 1
    return answer


for t in range(T):
    n, m = [int(_) for _ in input().split()]
    M = []
    count_G = 0
    has_B = False
    for i in range(n):
        row = [_ for _ in input()]
        count_G += row.count('G')
        if 'B' in row:
            has_B = True
        M.append(row)

    try:
        if not count_G:
            if M[n - 1][m - 1] == 'B':
                print('No')
            else:
                print('Yes')
        else:
            for i in range(len(M)):
                for j in range(len(M[0])):
                    if M[i][j] == 'B':
                        for x, y in neighbours(M, i, j):
                            if M[x][y] == '.':
                                M[x][y] = '
                            elif M[x][y] == 'G':
                                print('No')
                                raise Found()
            accessible_G = bfs(M, n - 1, m - 1)
            if accessible_G == count_G:
                print('Yes')
            else:
                print('No')
    except Found:
        pass
