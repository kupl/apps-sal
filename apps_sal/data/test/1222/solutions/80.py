from collections import deque
K = int(input())
q = deque()
for i in range(1, 10):
    q.append(i)
ans = 0
if K >= 10:
    cnt = 9
    while len(q) > 0:
        current = q.popleft()
        dn = [-1, 0, 1]
        for i in dn:
            if current % 10 + i < 0 or current % 10 + i > 9 or cnt >= K:
                continue
            q.append(current * 10 + current % 10 + i)
            cnt += 1
    else:
        ans = current
else:
    ans = K
print(ans)
