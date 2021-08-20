from collections import deque
(n, d) = map(int, input().split())
friends = sorted((tuple(map(int, input().split())) for _ in range(n)))
ss = deque()
mm = deque()
ff = 0
ans = 0
for (m, s) in friends:
    ss.append(s)
    mm.append(m)
    ff += s
    while mm[0] + d <= mm[-1]:
        ff -= ss.popleft()
        mm.popleft()
    ans = max(ans, ff)
print(ans)
