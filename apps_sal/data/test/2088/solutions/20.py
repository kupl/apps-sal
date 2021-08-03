from collections import defaultdict
import sys
input = sys.stdin.readline
graph = defaultdict(list)
n = int(input())
par = [int(i) for i in input().split() if i != '\n']
bulb = [1] * (n + 1)
for i in range(n - 1):
    bulb[par[i]] = 0
    graph[par[i]].append(i + 2)
# print(graph,bulb,par)
zero = bulb.count(0)
for i in range(n, 0, -1):
    if bulb[i] == 0:
        count = 0
        for j in graph[i]:
            count += bulb[j]
        bulb[i] = count
bulb = bulb[1:]
bulb.sort()
sys.stdout.write(' '.join(map(str, bulb)))
