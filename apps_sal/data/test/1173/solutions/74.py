from collections import deque

N = int(input())
A = [deque([a - 1 for a in map(int, input().split())]) for _ in range(N)]
cnt = 0
cur = [-1 for _ in range(N + 1)]
day = [0 for _ in range(N + 1)]
que = deque(range(N))

while que:
    x = que.popleft()
    if not A[x]:
        continue
    y = A[x].popleft()
    if cur[y] == x:
        cnt += 1
        day[x] = day[y] = max(day[x], day[y]) + 1
        cur[x] = cur[y] = -1
        que.append(x), que.append(y)
    else:
        cur[x] = y

flag = (cnt == N * (N - 1) / 2)
print(max(day) if flag else -1)
