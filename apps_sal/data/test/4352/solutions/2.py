(a, b) = map(int, input().split())
st_l = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
if st_l.index(a) > st_l.index(b):
    print('Alice')
elif st_l.index(a) < st_l.index(b):
    print('Bob')
else:
    print('Draw')
