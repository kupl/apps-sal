from collections import deque
n = int(input())
mins = [1000 for i in range(n + 1)]
used = [0 for i in range(n + 1)]
deq = deque()
deq.append((1, 1))
while deq:
    x, cnt = deq.popleft()
    mins[x] = min(mins[x], cnt)
    used[x] = 1
    if used[10 * x % n] == 0:
        deq.appendleft((10 * x % n, cnt))
    if used[(x + 1) % n] == 0:
        deq.append(((x + 1) % n, cnt + 1))
print(mins[0])
