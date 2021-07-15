from itertools import product

N, W = map(int,input().split())
L = [[] for _ in range(4)]
w, v = map(int,input().split())
L[0].append(v)
for _ in range(N-1):
    tmp_w, tmp_v = map(int,input().split())
    L[tmp_w - w].append(tmp_v)

for i in range(4):
    L[i].sort(reverse = True)

for i in range(4):
    for j in range(len(L[i]) - 1):
        L[i][j+1] += L[i][j]
    L[i] = [0] + L[i]

ans = 0

for i, j, k, l in product(range(len(L[0])), range(len(L[1])), range(len(L[2])), range(len(L[3]))):
   if w * (i + j + k + l) + j + 2 * k + 3 * l <= W:
        ans = max(ans, L[0][i] + L[1][j] + L[2][k] + L[3][l])

print(ans)
