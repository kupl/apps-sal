import sys
readline = sys.stdin.readline

H, W, K = map(int, readline().split())
grid = [None] * (H + 1)
grid[0] = [0] * (W + 1)
for i in range(1, H + 1):
    grid[i] = [0] + list(map(int, list(input())))


for i in range(len(grid) - 1):
    for j in range(len(grid[i])):
        grid[i + 1][j] = grid[i][j] + grid[i + 1][j]

for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
        grid[i][j + 1] = grid[i][j] + grid[i][j + 1]


def get_choco_cnt(i, j, p, q):
    return grid[i][j] - grid[i][q] - grid[p][j] + grid[p][q]


def isOk(x, lastq, cond, K, H, W):
    lastp = 0
    for j in range(H - 1):
        if (cond >> j) & 1:
            if get_choco_cnt(j + 1, x, lastp, lastq) > K:
                return False
            lastp = j + 1
    if get_choco_cnt(H, x, lastp, lastq) > K:
        return False
    return True


def decide_cut(cond, lastq, K, H, W):
    ok = lastq
    ng = W + 1
    while abs(ok - ng) > 1:
        mid = abs(ok + ng) // 2
        if isOk(mid, lastq, cond, K, H, W):
            ok = mid
        else:
            ng = mid
    return ok


ans = 10000
for cond in range(2 ** (H - 1)):
    cut_num = (bin(cond)[2:]).count("1")
    lastq = 0
    while lastq < W + 1:
        new_lastq = decide_cut(cond, lastq, K, H, W)
        if new_lastq == W:
            break
        if new_lastq == lastq:
            cut_num = 10000
            break
        cut_num += 1
        lastq = new_lastq
    if ans > cut_num:
        ans = cut_num
print(ans)
