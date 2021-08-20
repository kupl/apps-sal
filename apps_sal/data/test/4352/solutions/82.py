(e1, e2) = map(int, input().split())
a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
if e1 == e2:
    print('Draw')
elif a.index(e1) > a.index(e2):
    print('Alice')
else:
    print('Bob')
