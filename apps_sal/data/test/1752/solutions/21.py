import sys
sys.setrecursionlimit(10**5)

N = int(input())
*A, = map(int, input().split())

A.sort()
memo = [[-1]*(N+1) for i in range(N+1)]
nxt = [[0]*(N+1) for i in range(N+1)]
def dfs(i, p, q):
    if memo[p][q] != -1:
        return memo[p][q]
    if i == N:
        return abs(A[p] - A[q])
    r0 = max(dfs(i+1, i, q), abs(A[i] - A[p]))
    r1 = max(dfs(i+1, p, i), abs(A[i] - A[q]))
    if r0 < r1:
        nxt[p][q] = 0
    else:
        nxt[p][q] = 1
    memo[p][q] = r = min(r0, r1)
    return r
dfs(0, 0, 0)
R0 = []; R1 = []
p = q = 0
for i in range(N):
    if nxt[p][q]:
        R1.append(A[i])
        q = i
    else:
        R0.append(A[i])
        p = i
R0.reverse()
R0.extend(R1)
print(*R0)
