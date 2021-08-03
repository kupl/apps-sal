from collections import defaultdict
import heapq


INF = 10 ** 6


def check(N, adj_nodes, costs, from_node, to_node):
    # calculate shortest distances on a graph without a edge (from_node, to_node)
    dists = [INF for _ in range(N)]
    dists[from_node] = 0
    frontier = [(0, from_node)]
    while len(frontier) > 0:
        d, node = heapq.heappop(frontier)
        for next_node in adj_nodes[node]:
            if (from_node, to_node) == (node, next_node):
                continue
            next_d = costs[node][next_node] + dists[node]
            if dists[next_node] > next_d:
                dists[next_node] = next_d
                heapq.heappush(frontier, (next_d, next_node))
    return costs[from_node][to_node] > dists[to_node]


def main():
    N, M = list(map(int, input().split(' ')))
    adj_nodes = defaultdict(list)
    costs = [[INF for _ in range(N)] for _ in range(N)]
    edges = list()
    for _ in range(M):
        a, b, c = list(map(int, input().split(' ')))
        a -= 1
        b -= 1
        adj_nodes[a].append(b)
        adj_nodes[b].append(a)
        costs[a][b] = c
        costs[b][a] = c
        edges.append((a, b))
    ans = 0
    for edge in edges:
        from_node, to_node = edge
        if check(N, adj_nodes, costs, from_node, to_node):
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
