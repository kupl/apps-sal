import numpy as np
N, M, Q = map(int, input().split())  # N個の都市、M本の列車、Q個のクエリ
grid = np.zeros((N + 1, N + 1), dtype=np.int64)
query = []
for _ in range(M):
    L, R = map(int, input().split())
    grid[L, R] += 1
cum_grid = grid.cumsum(axis=0).cumsum(axis=1)

ans_list = []
for _ in range(Q):
    p, q = map(int, input().split())
    ans = cum_grid[q, q] - cum_grid[p - 1, q] - cum_grid[q, p - 1] + cum_grid[p - 1, p - 1]
    ans_list.append(ans)

for ans in ans_list:
    print(ans)
