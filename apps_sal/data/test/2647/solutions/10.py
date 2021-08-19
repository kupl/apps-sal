import numpy as np
H, W = map(int, input().split())
Grid = np.array([[0 if x == '.' else -1 for x in input()] for _ in range(H)], dtype='int64')


def solveMase(Grid, start, goal):  # bfsで迷路を解き、スタート-ゴール間の最低必要白マス数を返す
    seen = {start}
    V = [start]
    while len(V) != 0:  # bfs
        v = V.pop(0)
        if v == goal:
            return Grid[goal]
        # 移動先nvをリストにまとめる
        y, x = v
        nV = []
        if x > 0:
            nV.append((y, x - 1))
        if y > 0:
            nV.append((y - 1, x))
        if x < W - 1:
            nV.append((y, x + 1))
        if y < H - 1:
            nV.append((y + 1, x))
        # bfs
        for nv in nV:
            if Grid[nv] == -1 or nv in seen:
                continue
            Grid[nv] = Grid[v] + 1
            V.append(nv)
            seen.add(nv)
    return 0


white = len(Grid[Grid == 0]) - 1
nes_white = solveMase(Grid, (0, 0), (H - 1, W - 1))
print(white - nes_white if nes_white > 0 else -1)
