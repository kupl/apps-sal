row = col = -1


def problem_input() -> None:
    nonlocal row, col

    for i in range(5):
        index = input().find('1')

        if index >= 0:
            row = i
            col = index // 2


def count_moves(row_index: int, col_index: int) -> int:
    return abs(row_index - 2) + abs(col_index - 2)


problem_input()
print(count_moves(row, col))
