from collections import deque


K = int(input())
path = [K] * K

q = deque()
path[1] = 0
q.append(1)
while q:
    p = q.popleft()
    p1 = (p + 1) % K
    if path[p1] > path[p] + 1:
        path[p1] = path[p] + 1
        q.append(p1)
    
    p10 = (p * 10) % K
    if path[p10] > path[p]:
        path[p10] = path[p]
        q.appendleft(p10)

print((path[0] + 1))

