(n, k) = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())
result = [None] * n
for i in range(n):
    result[i] = [0] * n
for (r, row) in enumerate(board):
    for i in range(len(board) - k + 1):
        if row[i:i + k] == '.' * k:
            for x in range(i, i + k):
                result[r][x] += 1
for col in range(len(board)):
    for i in range(len(board) - k + 1):
        if ''.join([board[j][col] for j in range(i, i + k)]) == '.' * k:
            for x in range(i, i + k):
                result[x][col] += 1
_max = 0
max_pos = (0, 0)
for (r, row) in enumerate(result):
    for (c, col) in enumerate(row):
        if col > _max:
            max_pos = (r, c)
            _max = col
print('{} {}'.format(max_pos[0] + 1, max_pos[1] + 1))
