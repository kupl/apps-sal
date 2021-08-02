def main():
    n, m = [int(x) for x in input().split()]

    board = []
    cols = [0] * m
    rows = [0] * n
    total = 0
    for i in range(0, n):
        r = input()
        board.append(r)
        for j in range(0, m):
            if r[j] == '*':
                cols[j] += 1
                rows[i] += 1
                total += 1

    for i in range(0, n):
        for j in range(0, m):
            count = rows[i] + cols[j]
            if board[i][j] == '*':
                count -= 1
            if count == total:
                print("YES")
                print(i + 1, j + 1)
                return

    print("NO")


main()
