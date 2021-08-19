from collections import deque

# グラフに辺を追加する


def addEdge(adjL, vFr, vTo, cap):
    adjL[vFr].append([vTo, cap, len(adjL[vTo])])
    adjL[vTo].append([vFr, 0, len(adjL[vFr]) - 1])  # 逆辺


# Edmonds-Karp法（最大フローを求める）
def Edmonds_Karp(adjL, vSt, vEn):

    # 残余グラフの始点から終点までの経路（増加パス）を、BFSで探索する
    def BFS(vSt, vEn):
        prev = [-1] * numV
        prev[vSt] = None
        iE = [-1] * numV
        df = 0
        Q = deque([(vSt, float('inf'))])
        while Q:
            vNow, fNow = Q.popleft()
            if vNow == vEn:
                # 終点に到達したら、ループを抜ける
                df = fNow
                break

            for i, (v2, cap, iRev) in enumerate(adjL[vNow]):
                if prev[v2] == -1 and cap > 0:
                    # 未探索の頂点への辺の容量に空きがある場合、探索する
                    prev[v2] = vNow
                    iE[v2] = (i, iRev)
                    Q.append((v2, min(fNow, cap)))

        if df > 0:
            # 始点から終点までの経路を遡って、辺のフローを変更する
            vNow = vEn
            while vNow != vSt:
                v0 = prev[vNow]
                e, iRev = iE[vNow]
                adjL[v0][e][1] -= df
                adjL[vNow][iRev][1] += df
                vNow = v0

        # フローの増加量を返す
        return df

    numV = len(adjL)
    MaximumFlow = 0
    while True:
        # 残余グラフの始点から終点までの経路（増加パス）を、BFSで探索する
        df = BFS(vSt, vEn)

        if df == 0:
            # 経路が見つからない場合、最大フローの値を返す
            return MaximumFlow

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

# Edmonds-Karp法（最大フローを求める）
mf = Edmonds_Karp(adjList, 0, N + 1)
print((sum([A for A in As if A > 0]) - mf))
