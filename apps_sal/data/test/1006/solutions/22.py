from typing import List


def cross_neighbors(i: int, j: int):
    return [(i + 1, j - 1), (i + 1, j), (i + 1, j + 1), (i + 2, j)]


def solve(n: int, board: List[List[str]]) -> str:
    for i in range(0, n - 2):
        for j in range(1, n - 1):
            if board[i][j] == '
             board[i][j] = '.'
              for x, y in cross_neighbors(i, j):
                   if board[x][y] == '.':
                        return 'NO'
                    if board[x][y] == '
                     board[x][y] = '.'
    return ['YES', 'NO'][any(board[i][j] == '
                             for i in range(n) for j in range(n))]


n = int(input())
board = [list(input()) for _ in range(n)]

print(solve(n, board))
