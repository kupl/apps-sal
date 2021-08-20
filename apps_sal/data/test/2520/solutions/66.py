from collections import deque, Counter
import sys
N_MAX = 100000 + 5
sys.setrecursionlimit(N_MAX)
(N, M, K) = map(int, sys.stdin.readline().rstrip().split())
fr = [[] for _ in range(N)]
for _ in range(M):
    (a, b) = map(int, sys.stdin.readline().rstrip().split())
    fr[a - 1].append(b - 1)
    fr[b - 1].append(a - 1)
bl = [[] for _ in range(N)]
for _ in range(K):
    (a, b) = map(int, sys.stdin.readline().rstrip().split())
    bl[a - 1].append(b - 1)
    bl[b - 1].append(a - 1)
gr = [0] * N


def bfs(u, num):
    q = deque()
    q.append(u)
    gr[u] = num
    while q:
        u = q.popleft()
        for v in fr[u]:
            if gr[v] == 0:
                gr[v] = num
                q.append(v)


num = 1
for i in range(N):
    if gr[i] == 0:
        bfs(i, num)
        num += 1
gr_num = Counter(gr)
ans = []
for i in range(N):
    kouho_suu = gr_num[gr[i]]
    for f in fr[i]:
        if gr[i] == gr[f]:
            kouho_suu -= 1
    for b in bl[i]:
        if gr[i] == gr[b]:
            kouho_suu -= 1
    kouho_suu -= 1
    ans.append(kouho_suu)
print(*ans)
