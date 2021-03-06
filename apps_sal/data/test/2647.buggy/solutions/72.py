from collections import deque


def main():

    def _bfs():
        while q:
            now = q.popleft()
            (height, width) = (now[0], now[1])
            if height == h - 1 and width == w - 1:
                return board[height][width]
            for i in range(4):
                ny = height + dy[i]
                nx = width + dx[i]
                if 0 <= ny < h and 0 <= nx < w and (board[ny][nx] == '.'):
                    q.append((ny, nx))
                    board[ny][nx] = 1 + board[height][width]
        return -1
    (h, w) = list(map(int, input().split()))
    board = []
    totalPoints = 0
    for _ in range(h):
        row = list(input())
        totalPoints += row.count('.')
        board.append(row)
    board[0][0] = 1
    q = deque([(0, 0)])
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    step = _bfs()
    if step == -1:
        return -1
    ans = totalPoints - step
    return ans


def __starting_point():
    print(main())


__starting_point()
