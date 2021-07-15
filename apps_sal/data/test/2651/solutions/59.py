num = input().split(" ")
zahyou_x = input().split(" ")
zahyou_y = input().split(" ")
x_num = int(num[0])
y_num = int(num[1])
x_sum = 0
y_sum = 0

for i in range(x_num):
    x_sum += int(zahyou_x[i]) * (i*2 - x_num + 1)

for i in range(y_num):
    y_sum += int(zahyou_y[i]) * (i*2 - y_num + 1)
print(x_sum*y_sum%(10**9+7))
