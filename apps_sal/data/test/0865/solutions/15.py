import numpy as np
(n, t) = map(int, input().split())
lst = np.full(t, -float('inf'))
lst[0] = 0
ans = 0
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort()
for (a, b) in ab:
    ans = max(ans, max(lst) + b)
    if a < t:
        lst[a:] = np.maximum(lst[a:], lst[:-a] + b)
ans = int(ans)
print(ans)
