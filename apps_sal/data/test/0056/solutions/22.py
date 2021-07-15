def push(graph, pos, level):
    if graph[pos] > 1:
        over = graph[pos] - 1
        graph[pos] = 1
        if level + pos < numberofglasses:
            graph[level + pos] += over / 2
        if level + pos + 1 < numberofglasses:
            graph[level + pos + 1] += over / 2
        if level + pos < numberofglasses:
            push(graph, level + pos, level + 1)
        if level + pos + 1 < numberofglasses:
            push(graph, level + pos + 1, level + 1)


n, t = map(int, input().split())
table = dict()
current = 0
for i in range(1, 11):
    current += i
    table[i] = current
graph = [0] * table[n]
numberofglasses = table[n]

graph[0] += t
push(graph, 0, 1)
counter = 0
for elem in graph:
    if elem == 1:
        counter += 1
print(counter)
