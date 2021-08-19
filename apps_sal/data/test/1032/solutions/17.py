def smallest_winner(matrix, starting_x, x):
    for m in matrix:
        if m > x:
            starting_x += m - x
            x += m - x
        x += 1
    return starting_x


def biggest_winner(matrix, p, maxi):
    for i in range(len(matrix)):
        if i + p - 1 >= len(matrix):
            break
        maxi = min(maxi, matrix[i + p - 1] - i)
    return maxi


(n, p) = map(int, input().split())
matrix = sorted(list(map(int, input().split())))
res = [i for i in range(smallest_winner(matrix, 1, 1), biggest_winner(matrix, p, matrix[-1]))]
print(len(res))
print(' '.join(map(str, res)))
