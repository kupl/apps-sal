n, m = list(map(int, input().split()))

board = [list(input()) for _ in range(n)]

ns = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

valid = True

for x, row in enumerate(board):
    for y, c in enumerate(row):
        b = 0
        for (dx, dy) in ns:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(row):
                if board[nx][ny] == '*':
                    b += 1
        xx = '.' if b == 0 else str(b)
        if c != '*' and xx != c:
            valid = False

print('YES' if valid else 'NO')
