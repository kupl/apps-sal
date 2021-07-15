from collections import deque

def bfs():
    # たどり着くまでにかかった回数をいれる多重リスト。
    d = [[float("inf")] * w for i in range(h)]
    # 1ノード降りるときにforで回せるようリスト化しておく
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 接したポイントを取り込む用のqueを定義
    que = deque([])
    # スタート地点をqueに加える。探索の際はqueから取り出すループを回すので最初だけ先に入れておく
    que.append((sx,sy))
    # スタートからスタートにかかる距離は0なのでinfを0にかえる。
    d[sx][sy] = 0
    # queがあるかぎり続ける
    while que:
        p = que.popleft()
        # 取り出した点がゴールなら終了
        if p[0] == gy and p[1] == gx:
            break
        #　それ以外の時は，接している点を4方向順に取得。一つずつ処理する。
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            # 新しく取得した座標に対しての処理
            # 迷路内に存在する座標であり，壁ではなく，まだ通ったことがなくdがinfの点なら処理する = 新しく取得した道候補の1つ
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
                # 道候補をqueに加える。
                que.append((nx, ny))
                # その道候補への経路までにかかった経路をdに加える。
                d[nx][ny] = d[p[0]][p[1]] + 1
    return d[gx][gy]

h, w = list(map(int, input().split()))
maze = [list(input()) for i in range(h)]
sx, sy = 0, 0
gx, gy = h - 1, w - 1

white = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == ".":
            white += 1

res = bfs()
if 0 < res < float("inf"):
    # 白いマスの数から最短経路でかかるコスト分を引く
    # ゴールを黒いマスに変えることはできないためその分も引く
    print((white - res - 1))
else:
    print((-1))

