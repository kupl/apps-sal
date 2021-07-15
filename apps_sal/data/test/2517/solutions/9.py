import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def warshallFloyd():
    for k in range(N):
        for i in range(N-1):
            for j in range(i, N):
                tmp = min(E[i][j], E[i][k] + E[k][j])
                E[i][j] = E[j][i] = tmp

def dfs(c, p, d):
    if c == R:
        ans[0] = min(ans[0], d)
        return
    for i in range(R):
        if used[i]:
            continue
        used[i] = True
        if p == -1:
            dfs(c+1, i, 0)
        else:
            dfs(c+1, i, d + E[S[p]-1][S[i]-1])
        used[i] = False

N, M, R = map(int, input().split())
S = list(map(int, input().split()))
E = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    E[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    E[a][b] = E[b][a] = c
warshallFloyd()
ans = [float('inf')]
used = [False] * R
dfs(0, -1, 0)
print(*ans)
