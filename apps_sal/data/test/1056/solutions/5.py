board = []
for i in range(10):
    board.append([int(i) for i in input().split()])

def next_squares(x, y):
    current_dir = 1 if x%2 else -1
    # print(x, y, current_dir)
    res = []
    for _ in range(6):
        nx, ny = x, y + current_dir
        if ny < 0 or ny == 10:
            nx, ny = x - 1, y
            current_dir *= -1
            if nx == -1: break
        x, y = nx, ny
        res.append([x, y])
    # print(x, y, res)
    return res



from functools import lru_cache

@lru_cache(None)
def dp(i, j, can_climb):
    if i == j == 0: return 0
    expected = []
    for x, y in next_squares(i, j):
        expected.append(dp(x, y, True))
    score = sum(expected) / len(expected) + (6 / len(expected))
    # print(i, j)
    if can_climb and board[i][j]: return min(score, dp(i - board[i][j], j, False))
    return score


print(dp(9, 0, True))
