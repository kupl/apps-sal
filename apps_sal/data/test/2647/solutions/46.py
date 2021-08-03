# config
from collections import deque
import sys
sys.setrecursionlimit(10**6)

# input
H, W = map(int, input().split())
maze = []
for _ in range(H):
    maze.append(input())


# スタートとゴール
si, sj = 0, 0
gi, gj = H - 1, W - 1

# 4近傍ベクトル↓→↑←
didj = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(H, W, blocker="X"):
    # queが空になったら探索終了
    while que != deque():
        i, j = que.popleft()
        for di, dj in didj:
            ni = i + di
            nj = j + dj
            # 遷移先ninjが不正でないか・壁でないか・まだ訪れたことがないかをチェック
            if 0 <= ni and ni < H and 0 <= nj and nj < W and maze[ni][nj] != blocker and d[ni][nj] == INF:
                d[ni][nj] = d[i][j] + 1
                que.append((ni, nj))
    return


INF = H * W * 10
d = [[INF for x in range(W)] for x in range(H)]
d[si][sj] = 0

# 最短経路探索開始
que = deque()
que.append((si, sj))
bfs(H, W, blocker="#")

# たどり着くとこができなかった場合
if d[gi][gj] == INF:
    print(-1)

# スコア出力
else:
    blc = 0
    for h in maze:
        for l in h:
            if l == "#":
                blc += 1
    score = H * W - blc - d[gi][gj] - 1  # 全マス数 - 壁の数 - 最短経路分 - スタートマスの分
    print(score)
