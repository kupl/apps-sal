import copy
import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
side = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
    side.append((a, b))


def dfs(v, G):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v] == True:
            continue
        dfs(next_v, G)


bridge = 0
# 各辺を取り除く
for a, b in side:
    Gc = copy.deepcopy(G)
    Gc[a].remove(b)
    Gc[b].remove(a)
    seen = [False] * N
    cnt = 0
    # 連結成分のカウント
    for s in range(N):
        if seen[s] == True:
            continue
        cnt += 1
        dfs(s, Gc)
    # 連結成分が 2 個以上ならその辺は橋
    if cnt >= 2:
        bridge += 1
print(bridge)
