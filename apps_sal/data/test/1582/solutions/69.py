import numpy as np
n = int(input())
graph = [[0] * 9 for i in range(9)]
for i in range(1, n + 1):
    if i % 10 != 0:
        i = str(i)
        sentou = int(i[0])
        matubi = int(i[-1])
        graph[sentou - 1][matubi - 1] += 1
graph = np.array(graph)
print(np.trace(np.dot(graph, graph)))
