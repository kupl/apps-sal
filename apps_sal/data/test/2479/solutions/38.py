def f_simplified_reversi():
    (N, Q) = [int(i) for i in input().split()]
    Queries = [[int(i) for i in input().split()] for j in range(Q)]
    (a, b) = ([N] * N, [N] * N)
    black_stone = (N - 2) ** 2
    (row, col) = (N, N)
    for (type, x) in Queries:
        if type == 1:
            if x < col:
                for i in range(x, col):
                    b[i] = row
                col = x
            black_stone -= b[x] - 2
        else:
            if x < row:
                for i in range(x, row):
                    a[i] = col
                row = x
            black_stone -= a[x] - 2
    return black_stone


print(f_simplified_reversi())
