W, H, N = [int(x) for x in input().split()]
x_min, x_max, y_min, y_max = 0, W, 0, H
num_lists = [[int(x) for x in input().split()] for _ in range(N)]

for num_list in num_lists:
    if num_list[2] == 1 and num_list[0] > x_min:
        x_min = num_list[0]
    if num_list[2] == 2 and num_list[0] < x_max:
        x_max = num_list[0]
    if num_list[2] == 3 and num_list[1] > y_min:
        y_min = num_list[1]
    if num_list[2] == 4 and num_list[1] < y_max:
        y_max = num_list[1]

if x_min > x_max or y_min > y_max:
    print(0)
else:
    print((x_max-x_min)*(y_max-y_min))
