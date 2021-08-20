from collections import deque
K = int(input())
q = deque()
q.append((1, 1))
visited = [False] * K
ans = 0
while ans == 0:
    (s, x) = q.popleft()
    if visited[x]:
        continue
    visited[x] = True
    if x == 0:
        ans = s
        break
    q.appendleft((s, 10 * x % K))
    q.append((s + 1, (x + 1) % K))
print(ans)
