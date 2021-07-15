from collections import deque

# グラフに辺を追加する
def addEdge(adjL, vFr, vTo, cap):
    adjL[vFr].append([vTo, cap, len(adjL[vTo])])
    adjL[vTo].append([vFr, 0, len(adjL[vFr]) - 1]) # 逆辺


# Dinic法（最大フローを求める）
def Dinic(adjL, vSt, vEn):

    # 始点からの最短距離を、BFSで求める
    def BFS(vSt):
        dist[vSt] = 0
        Q = deque([vSt])
        while Q:
            vNow = Q.popleft()

            for i, (v2, cap, iRev) in enumerate(adjL[vNow]):
                if dist[v2] == -1 and cap > 0:
                    # 未探索の頂点への辺の容量に空きがある場合、探索する
                    dist[v2] = dist[vNow] + 1
                    Q.append(v2)


    # 残余グラフの始点から終点までの経路（増加パス）を、DFSで探索する
    def DFS(vNow, vEn, fNow):
        if vNow == vEn:
            # 終点に到達したら、フローの増加量を返す
            return fNow

        # 前回の続きから、探索を再開する
        iSt = iNext[vNow]
        for i, (v2, cap, iRev) in enumerate(adjL[vNow][iSt:], iSt):
            if dist[vNow] < dist[v2] and cap > 0:
                # 始点からの最短距離が増加する頂点への辺の容量に空きがある場合、探索する
                df = DFS(v2, vEn, min(fNow, cap))
                if df > 0:
                    # 始点から終点までの経路を遡って、辺のフローを変更する
                    adjL[vNow][i][1] -= df
                    adjL[v2][iRev][1] += df
                    return df

            iNext[vNow] += 1

        # 現在の頂点からの探索先がない場合、ゼロを返す
        return 0


    numV = len(adjL)
    MaximumFlow = 0
    while True:
        # 始点からの最短距離を、BFSで求める
        dist = [-1] * numV
        BFS(vSt)
        if dist[vEn] == -1:
            # 終点までの経路が見つからない場合、最大フローの値を返す
            return MaximumFlow

        iNext = [0] * numV
        while True:
            # 残余グラフの始点から終点までの経路（増加パス）を、DFSで探索する
            df = DFS(vSt, vEn, float('inf'))

            if df == 0:
                # 経路が見つからない場合、ループを抜ける
                break

            # フローを加算する
            MaximumFlow += df


N = int(input())
As = list(map(int, input().split()))

adjList = [[] for v in range(N + 2)]
for i, A in enumerate(As, 1):
    if A <= 0:
        addEdge(adjList, 0, i, -A)
    else:
        addEdge(adjList, i, N + 1, A)

for i in range(1, N + 1):
    for j in range(2 * i, N + 1, i):
        addEdge(adjList, i, j, float('inf'))

# Dinic法（最大フローを求める）
mf = Dinic(adjList, 0, N + 1)
print((sum([A for A in As if A > 0]) - mf))

