from collections import deque
from itertools import accumulate
(n, k) = map(int, input().split())
l = list(map(int, input().split()))
l = [c - 1 for c in l]
l = [0] + l
cum = list(accumulate(l))
cum = [c % k for c in cum]
ans = 0
d = {}
q = deque()
for i in range(n + 1):
    if cum[i] not in d:
        d[cum[i]] = 1
    else:
        ans += d[cum[i]]
        d[cum[i]] += 1
    q.append(cum[i])
    if len(q) == k:
        rem = q.popleft()
        d[rem] -= 1
print(ans)
