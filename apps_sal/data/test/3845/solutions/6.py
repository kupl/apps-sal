def main():
    (A, B) = map(int, input().split())
    board = [['#'] * 100 for _ in range(50)] + [['.'] * 100 for _ in range(50)]
    wc = 1
    for i in range(0, 50, 2):
        for j in range(0, 100, 2):
            if wc >= A:
                break
            board[i][j] = '.'
            wc += 1
        if wc >= A:
            break
    bc = 1
    for i in range(51, 100, 2):
        for j in range(0, 100, 2):
            if bc >= B:
                break
            board[i][j] = '#'
            bc += 1
        if bc >= B:
            break
    print(100, 100)
    for r in board:
        print(*r, sep='')


main()
