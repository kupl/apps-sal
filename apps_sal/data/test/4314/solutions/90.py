def main():
    h, w = list(map(int, input().split()))
    board = []
    safe_h = set()
    safe_w = set()
    for i in range(h):
        board.append(list(input()))
    for i in range(h):
        for j in range(w):
            if board[i][j] == '#':
                safe_h.add(i)
                safe_w.add(j)
    for i in safe_h:
        for j in safe_w:
            print(board[i][j], end='')
        print()


def __starting_point():
    main()
__starting_point()
