def main():
    (rows, cols, k) = map(int, input().split())
    mat = [[0 for j in range(cols)] for i in range(rows)]
    is_one = [[False for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        vals = list(map(int, input().split()))
        for j in range(cols):
            is_one[i][j] = vals[j] == 1
            mat[i][j] += vals[j]
            if i - k >= 0:
                mat[i - k][j] -= vals[j]
    for j in range(cols):
        for i in range(rows - 2, -1, -1):
            mat[i][j] += mat[i + 1][j]
    max_score = 0
    min_moves = 0
    for j in range(cols):
        score = 0
        moves = 0
        best_moves = 0
        for i in range(rows):
            if not is_one[i][j]:
                continue
            if mat[i][j] > score:
                score = mat[i][j]
                best_moves = moves
            moves += 1
        max_score += score
        min_moves += best_moves
    print(max_score, min_moves)


main()
