trump = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
(a, b) = map(int, input().split(' '))
if a == b:
    print('Draw')
else:
    print(['Alice', 'Bob'][trump.index(b) > trump.index(a)])
