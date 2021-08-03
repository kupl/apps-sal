from collections import deque
H, W = map(int, input().split())
c = tuple(int(x) + 1 for x in input().split())
d = [int(x) + 1 for x in input().split()]
maze = [[-1] * (W + 4), [-1] * (W + 4)]

for i in range(H):
    temp = []
    s0 = input()
    s0 = '11' + s0.replace('.', '0').replace('#', '1') + '11'
    for j, s in enumerate(s0):
        temp.append(-int(s))
    maze.append(temp)
maze.append([-1] * (W + 4))
maze.append([-1] * (W + 4))


def check55(i, j):
    cset = {(ii, jj) for ii in range(i - 2, i + 3) for jj in range(j - 2, j + 3) if maze[ii][jj] == 0}
    cset = cset - {(i - 1, j), (i, j), (i + 1, j), (i, j - 1), (i, j + 1)}
    return cset


def check(i, j, delta):
    if delta[0] != 0:
        ii = i + 3 * delta[0]
        for jj in range(j - 2, j + 3):
            if maze[ii][jj] == 0:
                dset.add((ii, jj))

    else:
        jj = j + 3 * delta[1]
        for ii in range(i - 2, i + 3):
            if maze[ii][jj] == 0:
                dset.add((ii, jj))

    return

# bfs


k = 1
tempbfs = deque([[c[0], c[1], k]])
flag = 0
while tempbfs:
    if flag == 1:
        break
    p = tempbfs.popleft()

    # dfs
    if maze[p[0]][p[1]] != 0:
        continue
    maze[p[0]][p[1]] = p[2]
    if p[0] == d[0] and p[1] == d[1]:
        flag = 1
        k = p[2]
        break
    temp = [(p[0], p[1])]
    dset = set()
    while temp:
        p0 = temp.pop()
        for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y = p0[0] + delta[0]
            x = p0[1] + delta[1]
            if maze[y][x] != 0:
                continue
            maze[y][x] = p[2]
            if y == d[0] and x == d[1]:
                flag = 1
                k = p[2]
                break
            temp.append((y, x))
            check(p0[0], p0[1], delta)

    if flag == 1:
        break
    for l in dset:
        if maze[l[0]][l[1]] == 0:
            tempbfs.append([l[0], l[1], p[2] + 1])
    dset = check55(p[0], p[1])
    for l in dset:
        tempbfs.append([l[0], l[1], p[2] + 1])

print(k - 1 if flag else -1)
