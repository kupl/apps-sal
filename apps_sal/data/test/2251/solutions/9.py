def DFS(start, color):
    nonlocal isUsed
    isUsed[start] = True
    for i in graph[start]:
        if not isUsed[i[0]] and i[1] == color:
            DFS(i[0], color)

n, m = tuple(map(int, input().split()))

graph = [[] for i in range(n)]

for i in range(m):
    a, b, c = tuple(map(int, input().split()))
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

q = int(input())
answers = [0] * q
for i in range(q):
    u, v = tuple(map(int, input().split()))
    for j in range(1, m + 1):
        isUsed = [False] * n
        DFS(u - 1, j)
        if isUsed[v - 1]:
            answers[i] += 1

print("\n".join(map(str, answers)))

