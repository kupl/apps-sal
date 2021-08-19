# グラフのパスを全探索する関数(再帰)
def dfs(now_node, depth):  # deptt:今まで列挙した頂点数
    if seen[now_node]:  # 探索済みであった場合はreturn
        return 0
    if depth == N:  # 全ての頂点を通っていた場合、1を返す
        return 1
    seen[now_node] = True  # 今から探索するノードを探索済みにする
    connect_nodes = graph[now_node]
    ans = 0
    for node in connect_nodes:  # 全ての遷移先をチェックする
        ans += dfs(node, depth + 1)
    seen[now_node] = False  # 探索済みフラグを折る(ポイント)
    return ans


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]  # 辺の集合
graph = [[] for i in range(N + 1)]  # 隣接リスト
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# 訪問済みかどうかを表すリストを用意
seen = [False for i in range(N + 1)]
seen[0] = True

print(dfs(1, 1))
