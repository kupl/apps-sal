(n, m, x, y) = (int(i) for i in input().split())
list_x = sorted(list(map(int, input().split())))
list_y = sorted(list(map(int, input().split())))
if max(x, list_x[-1]) < min(y, list_y[0]):
    print('No War')
else:
    print('War')
