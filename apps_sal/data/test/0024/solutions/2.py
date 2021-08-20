a = []
for i in range(10):
    a.append(input())


def valid(x, y):
    if 0 <= x <= 9 and 0 <= y <= 9:
        return True
    return False


def check(x, y, direction):
    ans = 1
    curr_x = x + direction[0]
    curr_y = y + direction[1]
    while valid(curr_x, curr_y) and a[curr_x][curr_y] == 'X':
        ans += 1
        curr_x += direction[0]
        curr_y += direction[1]
    curr_x = x - direction[0]
    curr_y = y - direction[1]
    while valid(curr_x, curr_y) and a[curr_x][curr_y] == 'X':
        ans += 1
        curr_x -= direction[0]
        curr_y -= direction[1]
    return ans


curr = 0
for i in range(10):
    for j in range(10):
        if a[i][j] == '.':
            for direction in [[1, 0], [0, 1], [1, 1], [1, -1]]:
                curr = max(curr, check(i, j, direction))
if curr >= 5:
    print('YES')
else:
    print('NO')
