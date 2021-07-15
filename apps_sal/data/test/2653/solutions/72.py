import sys
sys.setrecursionlimit(10**8)
N, Q = map(int, input().split())
g = [[] for i in range(N)]
for i in range(N-1):
    a, b = list(map(int, input().split()))
    g[a-1].append(b-1)
    g[b-1].append(a-1)
cnt = [0] * N
for i in range(Q):
    p, x = list(map(int, input().split()))
    cnt[p-1] += x

def dfs(g, v):
    # nonlocal ans_cnt
    for nv in g[v]:
        if ans_cnt[nv] != -1: continue
        ans_cnt[nv] = cnt[nv] + ans_cnt[v]
        dfs(g, nv)

ans_cnt = [-1] * N
ans_cnt[0] = cnt[0]
dfs(g, 0)

# print(cnt)
# print(ans_cnt)
for i, value in enumerate(ans_cnt):
    print(value, end="")
    if i != len(ans_cnt)-1:
        print(" ", end="")
print()
