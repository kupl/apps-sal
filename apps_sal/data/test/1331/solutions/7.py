from collections import deque
(n, m, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
d = deque([])
ans = 0
for i in a:
    if len(d) > 0 and d[0] < i - m + 1:
        d.popleft()
    if len(d) < k - 1:
        d.append(i)
    else:
        ans += 1
print(ans)
