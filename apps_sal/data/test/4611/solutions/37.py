import sys
N = int(input())
t_param = 0
x_param = 0
y_param = 0

for i in range(N):
    t, x, y = map(int, input().split())
    if (abs(x - x_param) + abs(y - y_param))  > (abs(t - t_param)) or ((x + y + t)%2) != 0 :
        print('No')
        return
    t_param = t
    x_param = x
    y_param = y
print('Yes')
