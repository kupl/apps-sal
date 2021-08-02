from collections import deque
from itertools import product


H, W = list(map(int, input().split()))
S = [input() for _ in range(H)]
route = [[[[400 if S[si][sj] == S[ei][ej] == "." else -1 for ej in range(W)]for ei in range(H)]for sj in range(W)]for si in range(H)]

for i, j in product(list(range(H)), list(range(W))):
    if S[i][j] == ".":
        q = deque([[i, j, i, j]])
        break
while q:
    si, sj, ei, ej = q.pop()
    if (si, sj) == (ei, ej):
        route[si][sj][ei][ej] = 0
    d = route[si][sj][ei][ej]
    for p in [-1, 1]:
        if 0 <= si + p < H and route[si + p][sj][ei][ej] > d + 1:
            route[si + p][sj][ei][ej] = d + 1
            q.appendleft([si + p, sj, ei, ej])
        if 0 <= sj + p < W and route[si][sj + p][ei][ej] > d + 1:
            route[si][sj + p][ei][ej] = d + 1
            q.appendleft([si, sj + p, ei, ej])
        if 0 <= ei + p < H and route[si][sj][ei + p][ej] > d + 1:
            route[si][sj][ei + p][ej] = d + 1
            q.appendleft([si, sj, ei + p, ej])
        if 0 <= ej + p < W and route[si][sj][ei][ej + p] > d + 1:
            route[si][sj][ei][ej + p] = d + 1
            q.appendleft([si, sj, ei, ej + p])

print((max(route[si][sj][ei][ej] for si, sj, ei, ej in product(list(range(H)), list(range(W)), list(range(H)), list(range(W))))))
