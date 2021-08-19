from collections import defaultdict as dd
(H, W, N) = map(int, input().split())
Grid = dd(lambda: 0)


def Draw(x, y):
    return [(x - i, y - j) for i in range(3) for j in range(3) if 0 <= x - i < H - 2 and 0 <= y - j < W - 2]


for _ in range(N):
    (a, b) = map(int, input().split())
    for (x, y) in Draw(a - 1, b - 1):
        Grid[x, y] += 1
Ans = [(H - 2) * (W - 2) - len(Grid) if i == 0 else sum((v == i for v in Grid.values())) for i in range(10)]
for ans in Ans:
    print(ans)
