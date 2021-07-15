from itertools import permutations
from bisect import bisect_left, bisect_right
N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
L = [tuple(map(int, input().split())) for _ in range(M)]
L.sort(key=lambda x: x[1])
length = [0]
weights = [0]
for l, w in L:
    if l >= length[-1] and w >= weights[-1]:
        length.append(l)
        weights.append(w)

if max(W) > weights[1]:
    print((-1))
    return

ans = 10**10
for p in permutations(list(range(N))):
    rows = [0]*N
    V = [0]
    for i in range(N):
        V.append(V[-1]+W[p[i]])
    for i in range(N):
        for j in range(i+1, N):
            w = V[j+1]-V[i]
            rows[j] = max(rows[j], rows[i]+length[bisect_left(weights, w)-1])
    if ans > rows[-1]:
        ans = rows[-1]
print(ans)

