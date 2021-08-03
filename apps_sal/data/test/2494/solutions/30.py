from collections import deque
k = int(input())
t = [1] * k
q = deque()
q.append((1, 1))
while q:
    p, r = q.popleft()
    if p == 0:
        print(r)
        break
    if t[p]:
        t[p] = 0
        q.appendleft(((p * 10) % k, r))
        q.append(((p + 1) % k, r + 1))
