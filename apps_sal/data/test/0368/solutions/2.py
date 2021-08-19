board = list(input() + input() + input() + input() + input() + input() + input() + input())
w = 0
b = 0
w += 9 * board.count('Q')
w += 5 * board.count('R')
w += 3 * board.count('N')
w += 3 * board.count('B')
w += board.count('P')
b += 9 * board.count('q')
b += 5 * board.count('r')
b += 3 * board.count('n')
b += 3 * board.count('b')
b += board.count('p')
if w > b:
    print('White')
elif w == b:
    print('Draw')
else:
    print('Black')
