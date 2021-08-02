from itertools import product

N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

MAX = -10**12
for p in product(range(2), repeat=10):
    if p == (0,) * 10: continue
    SUM = 0
    for i in range(N):
        count = 0
        for j in range(10):
            if p[j] == 1 and F[i][j] == 1:
                count += 1
        SUM += P[i][count]
    MAX = max(MAX, SUM)
print(MAX)
