(n, m, x, y) = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))
if max(x_list) < min(y_list) and max(x_list) < y and (x < min(y_list)):
    print('No War')
else:
    print('War')
