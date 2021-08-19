def main():
    (n, k) = [int(x) for x in input().split()]
    board = []
    count = [[0 for i in range(n)] for j in range(n)]
    (m, x, y) = (0, 0, 0)
    for i in range(n):
        board.append(input())
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                if j + k - 1 < n and board[i][j + k - 1] == '.':
                    for l in range(j, j + k):
                        if board[i][l] == '#':
                            break
                    else:
                        for l in range(j, j + k):
                            count[i][l] += 1
                if i + k - 1 < n and board[i + k - 1][j] == '.':
                    for l in range(i, i + k):
                        if board[l][j] == '#':
                            break
                    else:
                        for l in range(i, i + k):
                            count[l][j] += 1
            if count[i][j] > m:
                m = count[i][j]
                (x, y) = (i, j)
    print(x + 1, y + 1)


def __starting_point():
    main()


__starting_point()
