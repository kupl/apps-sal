def main():
    (N, Q) = [int(v) for v in input().split()]
    Query = [[int(v) - 1 for v in input().split()] for _ in range(Q)]
    rows = [N - 1] * (N - 1)
    cols = [N - 1] * (N - 1)
    black = (N - 2) * (N - 2)
    min_row = N - 1
    min_col = N - 1
    for (ty, x) in Query:
        if ty == 0:
            if x < min_col:
                for j in range(x, min_col):
                    rows[j] = min_row
                min_col = x
            black -= rows[x] - 1
        else:
            if x < min_row:
                for j in range(x, min_row):
                    cols[j] = min_col
                min_row = x
            black -= cols[x] - 1
    print(black)


main()
