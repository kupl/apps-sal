from sys import stdin, stdout
input = stdin.readline

n, m = map(int, input().split())
graph =[set([]) for _ in range(n)]
popularity = [0 for _ in range(n)]

connections = []
for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    graph[x].add(y)
    graph[y].add(x)
    popularity[x] += 1
    popularity[y] += 1
    connections.append((x,y))

best = 100500
for x,y in connections:
    for el in graph[x] & graph[y]:
        best = min(popularity[x] + popularity[y] + popularity[el] - 6, best)

if best == 100500:
    stdout.write("-1")
else:
    stdout.write(str(best))
