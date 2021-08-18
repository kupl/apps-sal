n, m = list(map(int, input().split()))

g = [[] for _ in range(n)]
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(m):
    x, y = list(map(int, input().split()))

    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)
visited = [0] * n
for i in range(n):
    if not visited[i]:
        stack = [i]
        curr = 0
        visited[i] = 1
        while stack:
            node = stack.pop()
            curr += a[node] - b[node]
            for j in g[node]:
                if not visited[j]:
                    visited[j] = 1
                    stack.append(j)
        if curr:
            print('No')
            return

print("Yes")
