import itertools

n, m, k = list(map(int, input().split()))
field = [[False] * m for index in range(n)]
deltas = (
    ((0, -1), (-1, -1), (-1, 0)),  # Top left.
    ((-1, 0), (-1, 1), (0, 1)),   # Top right.
    ((0, 1), (1, 1), (1, 0)),     # Bottom right.
    ((1, 0), (1, -1), (0, -1)),   # Bottom left.
)
found = False
for index in range(k):
    i, j = [int(s) - 1 for s in input().split()]
    if not found:
        if not field[i][j]:
            for d in deltas:
                def f(di, dj): return 0 <= i + di < n and 0 <= j + dj < m and field[i + di][j + dj]
                if all(itertools.starmap(f, d)):
                    print(index + 1)
                    found = True
                    break
        field[i][j] = True
if not found:
    print(0)
