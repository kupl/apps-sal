
def dijkstra(node, edge, check):
    """
    nodeを含む連結グラフの中で、
    矛盾が発生しないか確認する
    矛盾が発生しない場合、
    nodeを0としたときの各ノードのスコアを返す
    """
    # 到達距離
    d = dict()
    st = [(node, 0)]
    curr_min = float('inf')
    curr_max = -float('inf')
    while st:
        curr_node, curr_d = st.pop()
        # 到達済みであれば矛盾が発生しないか確認する
        if curr_node in d.keys():
            if d[curr_node] != curr_d:
                # 矛盾が発生した
                return None, None, None, check
            else:
                continue
        # 到達した距離を記録
        d[curr_node] = curr_d 
        check[curr_node] = True
        if curr_d < curr_min:
            curr_min = curr_d
        if curr_max < curr_d:
            curr_max = curr_d

        # 隣接ノードを積む
        for nxt, diff in edge[curr_node]:
            st.append((nxt, curr_d + diff))
    
    return d, curr_min, curr_max, check


def submit():
    n, m = (int(e) for e in input().split())
    
    # グラフを構成
    edge = {i : [] for i in range(1, n + 1)}
    for _ in range(m):
        l, r, d = (int(e) for e in input().split())
        edge[l].append((r, d))
        edge[r].append((l, -d))

    check = {i: False for i in range(1, n + 1)}
    curr_max = -float('inf')

    for i in range(1, n + 1):
        if not check[i]:
            d, sub_min, sub_max, check = dijkstra(i, edge, check)

            if d == None:
                print('No')
                return
            # sub_minを0としたときのsub_maxを計算する
            sub_max -= sub_min
            if sub_max > curr_max:
                curr_max = sub_max

    if curr_max > 10 ** 9:
        print('No')
    else:
        print('Yes')


submit()
