def best_for_column(matrix, col) -> (int, int):
    """
    Finds the best solution for the given golumn
    :return: The score and the replacement count for this column
    """
    result_by_row = {

    }
    for row in range(n):
        if matrix[row][col] == 1:
            # We're on a 1, start counting rows downwards
            result_by_row[row] = 1
            upper_bound = min(row+k, n)  # either + K or the end (n)
            for r2 in range(row + 1, upper_bound):
                if matrix[r2][col] == 1:
                    result_by_row[row] += 1

    rows = list(sorted(result_by_row.keys()))

    # Find the best result and calculate the replacements for this one
    best_result = None
    for row in rows:
        if best_result is None or best_result['result'] < result_by_row[row]:  # always pick the top one for least replacements
            best_result = {'result': result_by_row[row], 'idx': row}
    if best_result is None:
        return 0, 0

    # Calculate the replacements for the best result
    replacements = 0
    idx = best_result['idx']
    for row in rows:
        if row < idx:
            replacements += 1
        else:
            break

    return best_result['result'], replacements

n, m, k = [int(p) for p in input().split()]
matrix = []
for i in range(n):
    matrix.append([int(p) for p in input().split()])


overall_result = 0
overall_replacements = 0
for col in range(m):
    # Go down on col
    # print(f'On col {# col}')
    res, repl = best_for_column(matrix, col)
    overall_result += res
    overall_replacements += repl
print("{} {}".format(overall_result, overall_replacements))
