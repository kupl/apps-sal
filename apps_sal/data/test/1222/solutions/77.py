from queue import deque
k = int(input())
que = deque()
for i in range(1, 10):
    que.append(i)
for i in range(k):
    now = que.popleft()
    too = now % 10
    if too != 0:
        que.append(now * 10 + too - 1)
    que.append(now * 10 + too)
    if too != 9:
        que.append(now * 10 + too + 1)
print(now)
