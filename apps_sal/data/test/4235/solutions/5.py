graph = [[] for _ in range(200000)]
colors = [0] * 200000
vis = [0] * 200000

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    colors[0] = 1
    queue = [(0, 1)]
    i = 0
    while i != len(queue):
        for v in graph[queue[i][0]]:
            if not colors[v]:
                colors[v] = 3 - queue[i][1]
                queue.append((v, colors[v]))
        i += 1
    
    ans = ['0'] * m
    for i in range(m):
        if colors[edges[i][0]] == colors[edges[i][1]]:
            print("NO")
            return 0
        if colors[edges[i][0]] == 1:
            ans[i] = '1'
    print("YES")
    print("".join(ans))
    return 0
main()
