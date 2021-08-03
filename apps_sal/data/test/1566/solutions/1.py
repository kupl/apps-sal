import sys
import math


def bfs(x, y):
    Q = [[x, y]]
    ptr = 0
    min_ = [1000, 1000]
    max_ = [0, 0]
    while ptr < len(Q):
        v = Q[ptr]
        ptr += 1
        x = v[0]
        y = v[1]
        if matrix[x][y] == 4:
            used[x][y] = 1
            if x + 1 < n:
                if used[x + 1][y] == 0:
                    Q.append([x + 1, y])
                    used[x + 1][y] = 1
            if x - 1 > -1:
                if used[x - 1][y] == 0:
                    Q.append([x - 1, y])
                    used[x - 1][y] = 1
            if y + 1 < n:
                if used[x][y + 1] == 0:
                    Q.append([x, y + 1])
                    used[x][y + 1] = 1
            if y - 1 > -1:
                if used[x][y - 1] == 0:
                    Q.append([x, y - 1])
                    used[x][y - 1] = 1
            if x < min_[0] or (x == min_[0] and y < min_[1]):
                min_ = [x, y]
            if x > max_[0] or (x == max_[0] and y > max_[1]):
                max_ = [x, y]
        else:
            used[x][y] = 0
    for i in range(min_[0], max_[0] + 1):
        for j in range(min_[1], max_[1] + 1):
            if matrix[i][j] != 4:
                print('No')
                return
    for i in range(n):
        for j in range(n):
            if used[i][j] == 0 and matrix[i][j] >= 3:
                print('No')
                return
    # print('h')
    if min_[0] > 0:
        w = min_[0] - 1
        for j in range(min_[1], max_[1] + 1):
            used[w][j] = 1
            if matrix[w][j] != 2:
                print('No')
                return
    # print('h')
    if max_[0] < n - 1:
        w = max_[0] + 1
        for j in range(min_[1], max_[1] + 1):
            used[w][j] = 1
            if matrix[w][j] != 2:
                print('No')
                return
    if min_[1] > 0:
        w = min_[1] - 1
        for j in range(min_[0], max_[0] + 1):
            used[j][w] = 1
            if matrix[j][w] != 2:
                print('No')
                return
    # print('h')
    if max_[1] < n - 1:
        w = max_[1] + 1
        for j in range(min_[0], max_[0] + 1):
            used[j][w] = 1
            if matrix[j][w] != 2:
                print('No')
                return
    if min_[0] > 0 and min_[1] > 0:
        x = min_[0] - 1
        y = min_[1] - 1
        if matrix[x][y] != 1:
            print('No')
            return
        used[x][y] = 1
    if max_[0] < n - 1 and max_[1] < n - 1:
        x = max_[0] + 1
        y = max_[1] + 1
        if matrix[x][y] != 1:
            print('No')
            return
        used[x][y] = 1
    if min_[0] > 0 and max_[1] < n - 1:
        x = min_[0] - 1
        y = max_[1] + 1
        if matrix[x][y] != 1:
            print('No')
            return
        used[x][y] = 1
    if max_[0] < n - 1 and min_[1] > 0:
        x = max_[0] + 1
        y = min_[1] - 1
        if matrix[x][y] != 1:
            print('No')
            return
        used[x][y] = 1
    for i in range(n):
        for j in range(n):
            if used[i][j] == 1:
                continue
            elif matrix[i][j] != 0:
                print('No')
                return
    print('Yes')


n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    z = input()
    for j in range(n):
        matrix[i][j] = int(z[j])
used = [[0] * n for i in range(n)]
flag = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 4:
            flag = 1
            x = i
            y = j
            break
    if flag:
        break
if not flag:
    print('No')
    return
bfs(x, y)
