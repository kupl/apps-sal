board = dict(zip(input(), input()))
for c in input():
    if c.lower() not in board:
        print(c, end='')
    elif c.isupper():
        print(board[c.lower()].upper(), end='')
    else:
        print(board[c], end='')
