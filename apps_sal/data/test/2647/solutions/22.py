H, W = map(int, input().split())
import numpy as np
Grid = np.array([[0 if x == '.' else -1 for x in input()] for _ in range(H)],dtype='int64')

def solveMase(Grid, start, goal):
    seen = {start}
    V = [start]
    while len(V) != 0:
        v = V.pop(0)
        if v == goal:
            return Grid[goal]

        y,x = v
        nV = []
        if x > 0: nV.append((y,x-1))
        if y > 0: nV.append((y-1,x))
        if x < W-1: nV.append((y,x+1))
        if y < H-1: nV.append((y+1,x))

        for nv in nV:
            if Grid[nv] == -1 or nv in seen:
                continue
            Grid[nv] = Grid[v] + 1
            V.append(nv)
            seen.add(nv)
    return 0

white = len(Grid[Grid == 0])-1
nes_white = solveMase(Grid, (0,0), (H-1,W-1))
if nes_white > 0:
    ans = white - nes_white
else:
    ans = -1
print(ans)
