import itertools
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]  # 辺の集合
graph = [[] for i in range(N + 1)]  # 隣接リスト
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

node = [i for i in range(1, N + 1)]
per_list = list(itertools.permutations(node))  # 順列生成
count = 0
for l in per_list:  # 全ての順列について条件を満たすかどうか探索
    if l[0] != 1:  # 開始ノードが1じゃなかったらダメ
        continue
    flg = 0
    for i in range(len(l) - 1):
        if not (l[i + 1] in graph[l[i]]):  # グラフの間に辺がなかったら
            flg = 1
            break
    if not flg:  # フラグがたってなかったら
        count += 1

print(count)
