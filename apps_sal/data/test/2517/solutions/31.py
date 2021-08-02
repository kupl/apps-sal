from scipy.sparse.csgraph import floyd_warshall
from itertools import permutations

N, M, R = map(int, input().split())

s = [[10**9] * N for i in range(N)]
t = list(map(int, input().split()))
for i in range(M):
    a, b, c = map(int, input().split())
    s[a - 1][b - 1] = c
    s[b - 1][a - 1] = c

s = floyd_warshall(s)
ans = float('inf')
for i in permutations(t):
    A_n = 0
    for j in range(R - 1):
        A_n += s[i[j] - 1][i[j + 1] - 1]
    ans = min(ans, A_n)

print(int(ans))
