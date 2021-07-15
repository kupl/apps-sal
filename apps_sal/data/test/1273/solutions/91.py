from collections import deque

def main():
    n = int(input())
    adj = [[]for i in range(n+1)]
    ab = [list(map(int, input().split())) for i in range(n-1)]
    for a, b in ab:
        adj[a].append(b)
        adj[b].append(a)
    # dequeを使ったスタックによるDFS
    # 子をindexで、親ノードを要素で
    # 今回は彩色のためにどんな順番でpopされたかも保持しておく
    order  = []
    parent = [0] * (n+1)
    visited = [0] * (n+1)
    visited[1] = 1
    q = deque([1])
    while q:
        par = q.popleft()
        order.append(par)
        for chl in adj[par]:
            if visited[chl]:
                continue
            # 行ったことなかったら1へ
            visited[chl] = 1
            parent[chl] = par
            q.append(chl)
    # 彩色
    # 親と同じにならないように若い番号を割り当てて行く
    cl = [None] * (n+1)
    for par in order:
        # 親の色
        pc = cl[par]
        # 彩色は1以上k以下
        color = 1
        for chl in adj[par]:
            # 隣接リストの親は無視
            if chl == parent[par]:
                continue
            # 親の色と同じなら色を変える
            if pc == color:
                color += 1
            # カラーリストに子indexにcolorを入れる
            cl[chl] = color
            #　他の子は色を変える必要がある
            color += 1
    # 木グラフなので単純に次数最大で考えて問題ない
    g = max([len(i) for i in adj]) 
    print(g)   
    for a, b in ab:
        # 親子関係が逆転しない出力ならこれでいいがそうとも限らない 
        if parent[a] != b:
            print(cl[b])
        else:
            print(cl[a])
            
def __starting_point():
    main()
__starting_point()
