(n, m, k) = [int(p) for p in input().split()]
matrix = []
for i in range(n):
    matrix.append([int(p) for p in input().split()])


def best(col):
    results = {}
    for row in range(n):
        if matrix[row][col] == 1:
            results[row] = 1
            for r2 in range(row + 1, min(row + k, n)):
                if matrix[r2][col] == 1:
                    results[row] += 1
    rows = list(sorted(results.keys()))
    best_result = None
    for row in rows:
        if best_result is None or best_result['res'] < results[row]:
            best_result = {'res': results[row], 'idx': row}
    if best_result is None:
        return (0, 0)
    replacements = 0
    idx = best_result['idx']
    for row in rows:
        if row < idx:
            replacements += 1
    return (best_result['res'], replacements)


result = 0
replacements = 0
for col in range(m):
    (res, repl) = best(col)
    result += res
    replacements += repl
print('{} {}'.format(result, replacements))
