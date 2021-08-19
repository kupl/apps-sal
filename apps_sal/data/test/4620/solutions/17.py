n = int(input())
graph = []
time = 0
for i in range(n - 1):
    (c, s, f) = map(int, input().split())
    graph.append([i, c, s, f])


def shortest_path(start, end, times):
    if start == end:
        return times
    elif times <= graph[start][2]:
        times = graph[start][2] + graph[start][1]
        return shortest_path(start + 1, end, times)
    elif times % graph[start][3] == 0:
        times += graph[start][1]
        return shortest_path(start + 1, end, times)
    else:
        times = times + graph[start][3] - times % graph[start][3] + graph[start][1]
        return shortest_path(start + 1, end, times)


for i in range(n):
    print(shortest_path(i, n - 1, 0))
