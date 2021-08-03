def generate_board(size, color):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(color)
            color = 0 if color == 1 else 1
        board.append(row)
    return board


def distance_from(have, need):
    paint = 0
    for have_row, need_row in zip(have, need):
        for h, n in zip(have_row, need_row):
            if h != n:
                paint += 1
    return paint


def solution(n, pieces):
    white = generate_board(n, 0)
    black = generate_board(n, 1)
    grid = [
        (distance_from(p, white), distance_from(p, black))
        for p in pieces
    ]
    combinations = [
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0]
    ]

    return min(sum(
        grid[i][c]
        for i, c in enumerate(combo)
    )
        for combo in combinations
    )


def __starting_point():
    n = int(input())
    pieces = []
    for _ in range(4):
        pieces.append(list(
            list(map(int, input()))
            for _ in range(n)
        ))
        if _ < 3:
            input()
    print(solution(n, pieces))


__starting_point()
