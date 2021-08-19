import numpy as np
import sys
read = sys.stdin.read


def solve(stdin):
    (h, w, m) = stdin[:3]
    row = np.zeros(h, np.int)
    col = np.zeros(w, np.int)
    for i in range(3, m * 2 + 3, 2):
        (y, x) = stdin[i:i + 2] - 1
        row[y] += 1
        col[x] += 1
    max_cnt_y = max(row)
    max_cnt_x = max(col)
    max_pair = np.sum(row == max_cnt_y) * np.sum(col == max_cnt_x)
    for i in range(3, m * 2 + 3, 2):
        (y, x) = stdin[i:i + 2] - 1
        if row[y] == max_cnt_y and col[x] == max_cnt_x:
            max_pair -= 1
    return max_cnt_y + max_cnt_x - (max_pair == 0)


print(solve(np.fromstring(read(), dtype=np.int, sep=' ')))
