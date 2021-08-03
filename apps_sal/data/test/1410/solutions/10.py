def main():
    n = int(input())
    color1 = [int(elm) for elm in input().split(" ")]
    color2 = [int(elm) for elm in input().split(" ")]
    color3 = [int(elm) for elm in input().split(" ")]

    graph = {}
    for i in range(n):
        graph[i] = []

    num_adjs = [0 for i in range(n)]
    for _ in range(n - 1):
        p, q = map(int, input().split(" "))
        p -= 1
        q -= 1
        graph[p].append(q)
        graph[q].append(p)
        num_adjs[p] += 1
        num_adjs[q] += 1

    if max(num_adjs) >= 3:
        print(-1)
        return

    node_type = [0 for i in range(n)]
    first_nodes = [i for i, num_adj in enumerate(num_adjs) if num_adj == 1]
    if len(first_nodes) != 2:
        print(-1)
        return
    first_node, end_node = first_nodes

    junban = [first_node]
    parent = first_node
    jibun = graph[first_node][0]
    count = 0
    for i in range(n - 1):
        junban.append(jibun)
        #print(end_node, jibun)

        if i == n - 2:
            #assert jibun == end_node
            pass
        kids = graph[jibun]
        for kid in kids:
            if parent != kid:
                parent = jibun
                jibun = kid
                break
        count += 1

    colors = [color1, color2, color3]
    min_tensu = sum(color1) + sum(color2) + sum(color3)

    color_orders = [[0, 1, 2], [0, 2, 1], [1, 2, 0], [1, 0, 2], [2, 0, 1], [2, 1, 0]]
    for ci, color_order in enumerate(color_orders):
        cur_tensu = 0
        node_colors = [-1 for i in range(n)]
        for i, node_i in enumerate(junban):
            i = i % 3
            node_color = color_order[i]
            cost = colors[node_color][node_i]
            node_colors[node_i] = node_color
            cur_tensu += cost
        if cur_tensu < min_tensu:
            min_ci = ci
            min_tensu = cur_tensu
            min_node_colors = node_colors

    print(min_tensu)
    print(" ".join([str(elm + 1) for elm in min_node_colors]))


main()
