n = int(input())
c = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
graph = []
for i in range(n):
    graph.append([])
sorted_graph = []
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    if len(graph[a]) > 2 or len(graph[b]) > 2:
        print(-1)
        return

for j in range(n):
    if len(graph[j]) == 1:
        sorted_graph.append(j)
        sorted_graph.append(graph[j][0])
        for _ in range(n - 2):
            for connection in graph[sorted_graph[-1]]:
                if connection != sorted_graph[-2]:
                    sorted_graph.append(connection)
                    break
        break

sorted_graph_indexes = [-1] * len(sorted_graph)
for i in range(len(sorted_graph_indexes)):
    sorted_graph_indexes[sorted_graph[i]] = i

sum = -1
signsum = 0
addsum = 0
for sign in range(-1, 2, 2):
    for add in range(3):
        lsum = 0
        for i in range(n):
            lsum += c[(add + sorted_graph_indexes[i] * sign) % 3][i]
        if sum == -1 or sum > lsum:
            sum = lsum
            signsum = sign
            addsum = add

print(sum)
for i in range(n):
    print((addsum + sorted_graph_indexes[i] * signsum) % 3 + 1, end=' ')

