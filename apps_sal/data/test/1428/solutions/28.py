from itertools import *
N, C = map(int, input().split())
D = [list(map(int, input().split())) for c in range(C)]
G = [list(map(int, input().split())) for n in range(N)]
H = [C * [0] for n in range(3)]

for i in range(N):
    for j, k in enumerate(G[i]):
        H[(i + j) % 3][k - 1] += 1

ans = float("inf")

for i in permutations(range(C), 3):
    c = 0
    for j in range(3):
        for k in range(C):
            c += D[k][i[j]] * H[j][k]
    ans = min(ans, c)

print(ans)
