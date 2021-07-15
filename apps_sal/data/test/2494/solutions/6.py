import heapq

def generate_graph(K):
    return [{(i + 1) % K: 1, (i * 10) % K: 0} for i in range(K)]

def dijkstra(start, goal, graph):
    answer = [float("inf")] * len(graph)
    answer[start] = 0
    remains = sorted([[v, i] for i, v in enumerate(answer)])

    while remains:
        _, i = heapq.heappop(remains)
        for j, cost in list(graph[i].items()):
            if answer[j] > answer[i] + cost:
                answer[j] = answer[i] + cost
                heapq.heappush(remains, [answer[j], j])

    return answer[goal] + 1

K = int(input())
graph = generate_graph(K)
print(dijkstra(1, 0, graph))

