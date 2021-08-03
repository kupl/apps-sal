import sys
import itertools
sys.setrecursionlimit(10**6)

N, M = list(map(int, input().split()))
tmp = [x for x in range(1, N)]
Cases = itertools.permutations(tmp)
G = [[] for _ in range(N)]
seen = [0] * N

for _ in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


def solve(v, case, cnt, N):
    if cnt == N - 1:
        return True
    for nv in G[v]:
        if nv == case[cnt]:
            return solve(nv, case, cnt + 1, N)
    return False


ans = 0
for case in Cases:
    if solve(0, case, 0, N):
        ans += 1
print(ans)
