def col(currY, currX, m):
    y_vals = currY * (currY - 1) // 2
    total = y_vals * m
    x_vals = (currX + m + currX + 1) * m // 2
    total += x_vals * currY
    return total


def row(currY, currX):
    y_vals = currY * (currX + 1)
    total = y_vals
    x_vals = (currX + 1) * currX // 2
    total += x_vals
    return total


(m, b) = [int(val) for val in input().strip().split(' ')]
initX = b * m
max_v = curr_v = (initX + 1) * initX // 2
curr_y = 0
for curr_x in range(initX - m, -1, -m):
    curr_y += 1
    curr_v = curr_v - col(curr_y, curr_x, m) + row(curr_y, curr_x)
    if curr_v > max_v:
        max_v = curr_v
    else:
        print(max_v)
        break
