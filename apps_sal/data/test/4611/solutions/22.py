n = int(input())

t_pre = 0
x_pre = 0
y_pre = 0
for i in range(n):
    t, x, y = list(map(int, input().split()))
    if (t - t_pre) < abs(x - x_pre) + abs(y - y_pre):
        print('No')
        break
    if t % 2 != (x + y) % 2:
        print('No')
        break
    t_pre = t
    x_pre = x
    y_pre = y

    if i == n - 1:
        print('Yes')
