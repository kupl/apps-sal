(x, y, a, b, c) = [int(i) for i in input().split()]
red_list = [int(i) for i in input().split()]
green_list = [int(i) for i in input().split()]
non_col_list = [int(i) for i in input().split()]
red_list.sort()
green_list.sort()
non_col_list.sort()
eat_red = []
eat_green = []
for i in range(x):
    eat_red.append(red_list.pop())
for i in range(y):
    eat_green.append(green_list.pop())
ans_list = eat_green + eat_red + non_col_list
ans_list.sort()
ans = 0
for i in range(x + y):
    ans += ans_list.pop()
print(ans)
