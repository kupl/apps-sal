dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

H, W = map(int, input().split())
S = [input() for _ in range(H)]

result = [[0 if v == '.' else '

for i in range(H):
    for j in range(W):
        if S[i][j] != '.':
            continue
        for d in range(8):
            ni = i + dx[d]
            nj = j + dy[d]
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if S[ni][nj] == '
                result[i][j] += 1

for row in result:
    print(*row, sep='')
