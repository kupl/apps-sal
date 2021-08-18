n = int(input())
line = []
dp_left = []
dp_right = []
for i in range(n):
    x, y = map(int, input().split())
    line.append([x, y])
    if i == 0:
        dp_left.append([x, y])
    else:
        dp_left.append([max(dp_left[i - 1][0], x), min(dp_left[i - 1][1], y)])
for i in range(n - 1, -1, -1):
    if i == n - 1:
        dp_right.append(line[i])
    else:
        dp_right.append([max(dp_right[n - i - 2][0], line[i][0]), min(dp_right[n - i - 2][1], line[i][1])])

max_ans = max(max(0, dp_left[-2][1] - dp_left[-2][0]), max(0, dp_right[-2][1] - dp_right[-2][0]))
for i in range(1, n - 1):
    l = max(dp_left[i - 1][0], dp_right[n - i - 2][0])
    r = min(dp_left[i - 1][1], dp_right[n - i - 2][1])
    max_ans = max(max_ans, r - l)
print(max_ans)
