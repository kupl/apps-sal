import heapq
n, m = list(map(int, input().split()))
edges = dict()
ans = [0 for _ in range(m + 1)]
graph = [set() for _ in range(n)]


for i in range(m):
    a, b, c = list(map(int, input().split()))
    edges[i] = (a - 1, b - 1, c)
    graph[a - 1].add(i)
    graph[b - 1].add(i)

# (cost,done,node,edge)
for i in range(n):
    done = [True for _ in range(n)]
    D = [(0, 0, i, m), ]
    heapq.heapify(D)

    while D:
        d = heapq.heappop(D)
        cost, mark, node, edge = d

        if done[node]:
            done[node] = False
            ans[edge] = 1

            for g in graph[node]:
                a, b, c = edges[g]

                if b == node:
                    a, b = b, a

                if done[b]:
                    heapq.heappush(D, (cost + c, ans[g], b, g))

print((m - (sum(ans) - 1)))

