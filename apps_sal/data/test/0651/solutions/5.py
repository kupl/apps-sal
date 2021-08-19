import itertools as I

h, w = list(map(int, input().split()))
M = [list(input()) for _ in range(h)]
cmds = input()


def ok(x, y):
    return 0 <= x < w and 0 <= y < h and M[y][x] != '#'


start = None
end = None
for i in range(h):
    for j in range(w):
        if M[i][j] == 'S':
            start = (j, i)
        if M[i][j] == 'E':
            end = (j, i)

cnt = 0
for dirs in I.permutations([(1, 0), (0, 1), (-1, 0), (0, -1)]):
    x, y = start
    for c in cmds:
        dx, dy = dirs[int(c)]
        x += dx
        y += dy
        if not ok(x, y):
            break
        if M[y][x] == 'E':
            cnt += 1
            break
print(cnt)
