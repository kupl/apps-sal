n = int(input())
e = [list() for _ in range(n)]
for i in range(n - 1):
    (u, v, w) = map(int, input().split())
    e[u - 1] += [[v, w]]
    e[v - 1] += [[u, w]]
visited = [-1] * n
stack = [0]
visited[0] = 0
while stack:
    z = stack.pop()
    for (v, w) in e[z]:
        if visited[v - 1] == -1:
            stack.append(v - 1)
            if w % 2 == 0:
                visited[v - 1] = visited[z]
            else:
                visited[v - 1] = 1 - visited[z]
        else:
            continue
print(*visited, sep='\n')
