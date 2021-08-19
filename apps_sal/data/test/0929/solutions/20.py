def main():
    H, W = map(int, input().split())
    field = []
    for _ in range(H):
        line = list(map(int, input().split()))
        field.append(line)

    ans = []
    # zig-zag
    for i in range(H):
        if i % 2 == 0:
            for j in range(W):
                if field[i][j] % 2 == 1:
                    field[i][j] -= 1
                    if j != W - 1:
                        field[i][j + 1] += 1
                        ans.append((i + 1, j + 1, i + 1, j + 2))
                    elif i != H - 1:
                        field[i + 1][j] += 1
                        ans.append((i + 1, j + 1, i + 2, j + 1))

                    else:
                        field[i][j] += 1
        else:
            for j in range(W - 1, -1, -1):
                if field[i][j] % 2 == 1:
                    field[i][j] -= 1
                    if j != 0:
                        field[i][j - 1] += 1
                        ans.append((i + 1, j + 1, i + 1, j))
                    elif i != H - 1:
                        field[i + 1][j] += 1
                        ans.append((i + 1, j + 1, i + 2, j + 1))

                    else:
                        field[i][j] += 1
    print(len(ans))
    for line in ans:
        print(*line, sep=" ")


def __starting_point():
    main()


__starting_point()
