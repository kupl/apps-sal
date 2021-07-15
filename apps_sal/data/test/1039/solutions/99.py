import sys  
sys.setrecursionlimit(200000)

N = int(input())
adj = {}

adj = {i+1: [] for i in range(N)}

for i in range(N-1):
    a, b, c = map(int, input().split())

    adj[a].append((b, c))
    adj[b].append((a, c))

dis = [0] * N

def dfs(k, u, d):
    """
    u: kの親
    d: vとuの最短距離
    adj_v: vの隣接
    これらのじょうけんのもとでdisを更新する
    """
    dis[k-1] = d

    for p, pk_dis in adj[k]:
        if p != u:
            dfs(p, k, d+pk_dis)

Q, K = map(int, input().split())
dfs(K, -1, 0)

for i in range(Q):
  x, y = map(int, input().split())
  print(dis[x-1] + dis[y-1])
