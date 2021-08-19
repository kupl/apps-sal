from collections import deque
q = deque()
ans = {}
K = int(input())
q.append((1, 1))
while len(q):
    (resid, total) = q.popleft()
    if resid in ans:
        continue
    ans[resid] = total
    q.appendleft((resid * 10 % K, total))
    q.append(((resid + 1) % K, total + 1))
print(ans[0])
