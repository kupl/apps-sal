from collections import deque

que = deque()

K = int(input())

que.append((1, 1))
visited = {}

while len(que) != 0:
    num, step = que.popleft()
    if num in visited:
        continue
    visited[num] = step
    que.appendleft((num * 10 % K, step))
    que.append(((num + 1) % K, step + 1))

print(visited[0])
