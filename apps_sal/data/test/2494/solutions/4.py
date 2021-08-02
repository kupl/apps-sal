from collections import deque
K = int(input())
cost = [-1] * K
deq = deque([(1, 1)])
while deq:
    x, d = deq.popleft()
    if cost[x] >= 0: continue
    cost[x] = d
    if x == 0: break
    for y, c in [(10 * x % K, 0), ((x + 1) % K, 1)]:
        if c: deq.append((y, d + 1))
        else: deq.appendleft((y, d))
print(cost[0])
