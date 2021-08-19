from collections import defaultdict as dd
(H, W, N) = map(int, input().split())
Draw = [tuple(map(int, input().split())) for _ in range(N)]
Sq = dd(lambda: 0)


def In(x, y):
    return [(x - i, y - j) for i in range(3) for j in range(3) if 0 <= x - i < H - 2 and 0 <= y - j < W - 2]


for (a, b) in Draw:
    for (x, y) in In(a - 1, b - 1):
        Sq[x, y] += 1
Ans = [(H - 2) * (W - 2) - len(Sq)] + [sum((v == i for v in Sq.values())) for i in range(1, 10)]
for ans in Ans:
    print(ans)
