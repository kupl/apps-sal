def find_cycle_optimum(n, m, k, adj):
    path = [1]
    visited = [-1 for _ in range(n + 1)]
    visited[1] = 1
    while True:
        v = path[-1]
        visited[v] = len(path) - 1
        for w in adj[v]:
            if visited[w] == -1:
                path.append(w)
                break
            elif len(path) - visited[w] > k:
                return path[visited[w]::]


def main():
    n, m, k = [int(i) for i in input().split()]
    adj = [[] for i in range(n + 1)]
    for _ in range(m):
        u, v = [int(i) for i in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    c = find_cycle_optimum(n, m, k, adj)
    l = len(c)
    print(l)
    print(' '.join(str(v) for v in c))


main()
