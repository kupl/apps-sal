import heapq


def main():
    (n, m) = list(map(int, input().split()))
    graph_dict = {}
    for _ in range(m):
        (u, v) = list(map(int, input().split()))
        temp_list = graph_dict.get(u, [])
        temp_list.append(v)
        graph_dict[u] = temp_list
        temp_list = graph_dict.get(v, [])
        temp_list.append(u)
        graph_dict[v] = temp_list
    visit = [False] * (n + 1)
    (h, ret) = ([], [])
    heapq.heappush(h, 1)
    while h:
        u = heapq.heappop(h)
        if visit[u]:
            continue
        ret.append(u)
        visit[u] = True
        for v in graph_dict.get(u, []):
            if visit[v]:
                continue
            heapq.heappush(h, v)
    print(*ret)


def __starting_point():
    main()


__starting_point()
