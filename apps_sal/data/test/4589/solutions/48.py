m, n = map(int, input().split())

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

S = [input() for i in range(m)]

for i in range(m):
    for j in range(n):
        num = 0
        if not S[i][j] == '#':
            for d in range(8):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx < 0 or nx >= m:
                    continue
                if ny < 0 or ny >= n:
                    continue
                if S[nx][ny] == '#':
                    num += 1
            A = list(S[i])
            A[j] = str(num)
            S[i] = "".join(A)

for i in range(m):
    print(S[i])
