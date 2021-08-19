(r, c, n, k) = list(map(int, input().split()))
board = [[0 for col in range(c)] for row in range(r)]
for i in range(n):
    (x, y) = [int(x) - 1 for x in input().split()]
    board[x][y] = 1
photos = 0
for x1 in range(r):
    for y1 in range(c):
        for x2 in range(x1, r):
            for y2 in range(y1, c):
                s = 0
                for row in range(x1, x2 + 1):
                    s += sum(board[row][y1:y2 + 1])
                if s >= k:
                    photos += 1
print(photos)
