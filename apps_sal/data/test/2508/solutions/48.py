from collections import deque


def resolve():
    H, W, K = map(int, input().split())
    ys, xs, yg, xg = map(int, input().split())

    board = [['@'] * (W + 2)]
    for i in range(H):
        board.append(['@'] + list(input()) + ['@'])
    board.append(['@'] * (W + 2))
    board[ys][xs] = '

    queue = deque([(xs, ys, 0)])
    while queue:
        x, y, dep = queue.popleft()
        l = []
        f1 = True
        f2 = True
        f3 = True
        f4 = True
        for i in range(1, K + 1):
            if f1:
                if board[y][x + i] == '.':
                    l.append((x + i, y))
                elif board[y][x + i] == '@' or board[y][x + i] != dep + 1:
                    f1 = False
            if f2:
                if board[y][x - i] == '.':
                    l.append((x - i, y))
                elif board[y][x - i] == '@' or board[y][x - i] != dep + 1:
                    f2 = False
            if f3:
                if board[y + i][x] == '.':
                    l.append((x, y + i))
                elif board[y + i][x] == '@' or board[y + i][x] != dep + 1:
                    f3 = False
            if f4:
                if board[y - i][x] == '.':
                    l.append((x, y - i))
                elif board[y - i][x] == '@' or board[y - i][x] != dep + 1:
                    f4 = False
            if not(f1 or f2 or f3 or f4):
                break
        for nx, ny in l:
            if board[ny][nx] == '.':
                board[ny][nx] = dep + 1
                if (nx, ny) == (xg, yg):
                    print(dep + 1)
                    return
                else:
                    queue.append((nx, ny, dep + 1))
    print(-1)
    return


resolve()
