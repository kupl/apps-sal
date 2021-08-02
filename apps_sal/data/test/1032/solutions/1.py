def smallest_winner(matrix):
    starting_x = 1
    x = 1
    for m in matrix:
        if m > x:
            starting_x += m - x
            x += m - x
        x += 1
    return starting_x


def biggest_winner(matrix, p):
    maxi = matrix[-1]
    for i in range(len(matrix)):
        if i + p - 1 >= len(matrix):
            break
        temp = matrix[i + p - 1] - i
        maxi = min(maxi, temp)
    return maxi


def check_multiple(matrix):
    count = 0
    maxi = 0
    for i in range(1, len(matrix)):
        if matrix[i] == matrix[i - 1]:
            count += 1
        else:
            count = 1
        maxi = max(maxi, count)
    return maxi


def solve(n, p, matrix):
    matrix = sorted(matrix)
    min_x = smallest_winner(matrix)
    max_x = biggest_winner(matrix, p) - 1
    return [i for i in range(min_x, max_x + 1)]


# T = int(input())
# for _ in range(T):
n, p = list(map(int, input().split()))
matrix = list(map(int, input().split()))
res = solve(n, p, matrix)
print(len(res))
print(" ".join(map(str, res)))
