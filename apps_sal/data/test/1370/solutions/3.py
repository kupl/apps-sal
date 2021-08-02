import sys
readline = sys.stdin.readline

H, W, K = map(int, readline().split())
grid = [None] * (H + 1)
grid[0] = [0] * (W + 1)
for i in range(1, H + 1):
    grid[i] = [0] + list(map(int, list(input())))

# 二次元累積和でチョコレートの数を管理
# 直前に選んだチョコのY座標をp,X座標をqとすると、
# チョコレートの数をO(1)で求められる
# 最初に空行を入れているので1-indexで。

for i in range(len(grid) - 1):
    for j in range(len(grid[i])):
        grid[i + 1][j] = grid[i][j] + grid[i + 1][j]

for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
        grid[i][j + 1] = grid[i][j] + grid[i][j + 1]


def get_choco_cnt(i, j, p, q):
    return grid[i][j] - grid[i][q] - grid[p][j] + grid[p][q]

# Hが10と少ないので、切る場所9箇所をすべて試しても2^9 = 512通り
# すべてに対して、Wのどこを切るかを求める。
# 二分探索なら　O(2^(H-1) * (log W * H)) = 約51200
# 線形探索でも　O(2^(H-1) * WH) = 5,120,000


def isOk(x, lastq, cond, K, H, W):
    # xで切ったとき、iで分割されたすべての領域の数がK以下になればOK
    lastp = 0  # Hを最後に切った場所
    for j in range(H - 1):
        if (cond >> j) & 1:  # j+1で切る
            if get_choco_cnt(j + 1, x, lastp, lastq) > K:
                return False
            lastp = j + 1
    # 最後に切った場所から、最後まで
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
    cut_num = (bin(cond)[2:]).count("1")  # カットした回数
    lastq = 0  # 最後にカットした場所
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
