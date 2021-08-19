from collections import Counter


def read_nums():
    return [int(x) for x in input().split()]


def read_board(n):
    board = []
    for _ in range(n):
        board.append(input())
    return board


def check_horizontal(board, boat_size, col_index, row_index):
    for i in range(col_index, col_index + boat_size):
        if i >= len(board):
            return False
        if board[row_index][i] == '#':
            return False
    return True


def check_vertical(board, boat_size, col_index, row_index):
    for i in range(row_index, row_index + boat_size):
        if i >= len(board):
            return False
        if board[i][col_index] == '#':
            return False
    return True


def main():
    n, k = read_nums()
    board = read_board(n)
    counter = Counter()
    for row_index in range(n):
        for col_index in range(n):
            if check_horizontal(board, k, col_index, row_index):
                for i in range(col_index, col_index + k):
                    counter[(row_index, i)] += 1
            if check_vertical(board, k, col_index, row_index):
                for i in range(row_index, row_index + k):
                    counter[(i, col_index)] += 1
    res = (0, 0)
    for k, v in list(counter.items()):
        if v > counter[res]:
            res = k

    print(res[0] + 1, res[1] + 1)


def __starting_point():
    main()


__starting_point()
