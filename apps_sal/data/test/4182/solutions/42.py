n, m, x, y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))
flag = False
if max(x_list) < min(y_list):
    flag = True
if flag:
    for i in range(max(x_list) + 1, min(y_list) + 1):
        if x < i <= y:
            flag = True
            break
        else:
            flag = False
if flag:
    print('No War')
else:
    print('War')
