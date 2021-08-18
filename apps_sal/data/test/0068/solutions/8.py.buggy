import sys
fin = sys.stdin.readline

n = int(fin())
commands = list(fin())[:-1]
x, y = [int(elem) for elem in fin().split(' ')]

move_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

if (x + y) % 2 != n % 2:
    print(-1)
    return

cuml_coord = [None] * n
cuml_x, cuml_y = 0, 0
for i, command in enumerate(commands):
    dx, dy = move_map[command]
    cuml_x += dx
    cuml_y += dy
    cuml_coord[i] = (cuml_x, cuml_y)

left, right = 0, 0
min_len = 2**32 - 1
org_x, org_y = cuml_coord[-1]
if org_x == x and org_y == y:
    min_len = 0

while right <= n - 1:
    if left == 0:
        left_cuml = 0, 0
    else:
        left_cuml = cuml_coord[left - 1]
    right_cuml = cuml_coord[right]
    movable_x, movable_y = right_cuml[0] - left_cuml[0], \
        right_cuml[1] - left_cuml[1]
    fixed_x, fixed_y = org_x - movable_x, org_y - movable_y
    sub_length = right - left + 1
    # print(fixed_x, fixed_y, left, right)
    # print(x - fixed_x, y - fixed_y)
    if (abs(x - fixed_x) + abs(y - fixed_y)) <= sub_length \
            and (abs(x - fixed_x) + abs(y - fixed_y)) % 2 == sub_length % 2:
        min_len = min(min_len, sub_length)
        if left != right:
            left += 1
        else:
            right += 1
    else:
        right += 1
if min_len == 2**32 - 1:
    print(-1)
else:
    print(min_len)
