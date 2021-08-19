from collections import deque
(n, m) = map(int, input().split())
h = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
ans = 0
for j in range(n):
    for i in g[j]:
        if h[j] <= h[i]:
            break
    else:
        ans += 1
print(ans)
