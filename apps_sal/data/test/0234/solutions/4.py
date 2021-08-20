def go():
    (n, m) = (int(i) for i in input().split(' '))
    board = []
    for i in range(n):
        board.append([i for i in input()])

    def get_neighbour_bombs(i, j):
        total = 0
        for k in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                if i + k >= n:
                    continue
                if i + k < 0:
                    continue
                if j + l >= m:
                    continue
                if j + l < 0:
                    continue
                if board[i + k][j + l] == '*':
                    total += 1
        return total
    for i in range(n):
        for j in range(m):
            if board[i][j] != '*':
                if board[i][j] == '.':
                    value = 0
                else:
                    value = int(board[i][j])
                if value != get_neighbour_bombs(i, j):
                    return 'NO'
    return 'YES'


print(go())
