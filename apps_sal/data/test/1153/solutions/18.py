(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
(cur_x, cur_y, index_x, index_y, result) = (x[0], y[0], 0, 0, 0)
while index_x < len(x) or index_y < len(y):
    if cur_x == cur_y:
        result += 1
        index_x += 1
        index_y += 1
        if index_x < len(x):
            cur_x = x[index_x]
        if index_y < len(y):
            cur_y = y[index_y]
    elif cur_x < cur_y:
        index_x += 1
        if index_x < len(x):
            cur_x += x[index_x]
    elif cur_x > cur_y:
        index_y += 1
        if index_y < len(y):
            cur_y += y[index_y]
print(result)
