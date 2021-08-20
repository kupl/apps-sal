from collections import deque
(n, m) = map(int, input().split())
G = [[] for _ in range(n)]
indeg = [0] * n
for _ in range(m):
    (l, r, d) = map(int, input().split())
    l -= 1
    r -= 1
    G[l].append((r, d))
    G[r].append((l, -d))
ng = False
visited = [0] * n
visited_cost = [0] * n
for start in range(n):
    if visited[start]:
        continue
    visited[start] = 1
    st = deque([[start, 0]])
    while st:
        (i, cost) = st.pop()
        for (ni, nd) in G[i]:
            if visited[ni] == 0:
                visited[ni] = 1
                visited_cost[ni] = cost + nd
                st.append([ni, cost + nd])
            elif visited_cost[ni] != cost + nd:
                ng = True
                break
        if ng:
            break
    if ng:
        break
print('No' if ng else 'Yes')
