def solve(n, k):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for right_move in range(n):
        for height in range(n):
            if k == 0:
                continue
            i = height
            j = (height + right_move) % n
            matrix[i][j] = 1
            k -= 1
    return matrix


def get_value(matrix):
    n = len(matrix)
    max_r = 0
    min_r = n
    max_c = 0
    min_c = n
    for line in matrix:
        value = sum(line)
        max_r = max(max_r, value)
        min_r = min(min_r, value)
    for j in range(n):
        value = sum([matrix[i][j] for i in range(n)])
        max_c = max(max_c, value)
        min_c = min(min_c, value)
    res = (max_r - min_r) ** 2
    res += (max_c - min_c) ** 2
    return res


T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    matrix = solve(n, k)
    value = get_value(matrix)
    print(value)
    for line in matrix:
        print(''.join(map(str, line)))

