n, k = list(map(int, input().split()))
s = [input() for _ in range(n)]
g_row = [[] for _ in range(n)]
g_col = [[] for _ in range(n)]

already_white_line_nums = 0
for i in range(n):
    for j in range(n):
        if s[i][j] == 'B':
            g_row[i].append(j)
            g_col[j].append(i)

for i in range(n):
    if not g_row[i]:
        already_white_line_nums += 1
    # else:
    #     g_row[i] = g_row[i][0], g_row[i][-1]
    if not g_col[i]:
        already_white_line_nums += 1
    # else:
    #     g_col[i] = g_col[i][0], g_col[i][-1]

r = 0

new_white_line_nums_col = [[[0] for _ in range(n - k + 1)] for _ in range(n - k + 1)]
# new_white_line_nums_row = [[[0] for _ in range(n - k + 1)] for _ in range(n - k + 1)]

for i in range(n - k + 1):
    new_white_line_nums = 0
    for l in range(0, k):
        if g_col[l] and i <= g_col[l][0] and g_col[l][-1] < i + k:
            new_white_line_nums += 1
    new_white_line_nums_col[i][0] = new_white_line_nums

    for old_col in range(n - k):
        if g_col[old_col] and i <= g_col[old_col][0] and g_col[old_col][-1] < i + k:
            new_white_line_nums -= 1
        new_col = old_col + k
        if g_col[new_col] and i <= g_col[new_col][0] and g_col[new_col][-1] < i + k:
            new_white_line_nums += 1
        new_white_line_nums_col[i][old_col + 1] = new_white_line_nums

for i in range(n - k + 1):
    new_white_line_nums = 0
    for l in range(0, k):
        if g_row[l] and i <= g_row[l][0] and g_row[l][-1] < i + k:
            new_white_line_nums += 1
    # new_white_line_nums_row[0][i] = new_white_line_nums
    r = max(r, new_white_line_nums_col[0][i] + new_white_line_nums)

    for old_row in range(n - k):
        if g_row[old_row] and i <= g_row[old_row][0] and g_row[old_row][-1] < i + k:
            new_white_line_nums -= 1
        new_row = old_row + k
        if g_row[new_row] and i <= g_row[new_row][0] and g_row[new_row][-1] < i + k:
            new_white_line_nums += 1
        r = max(r, new_white_line_nums_col[old_row + 1][i] + new_white_line_nums)
        # new_white_line_nums_row[old_row + 1][i] = new_white_line_nums

# r = 0
# for i in range(n - k + 1):
#     for j in range(n - k + 1):
#         r = max(r, new_white_line_nums_col[i][j] + new_white_line_nums_row[i][j])

print(r + already_white_line_nums)

