import itertools
from collections import defaultdict
(n, k) = map(int, input().split())
lis = list(map(int, input().split()))
lis = [0] + [lis[i] - 1 for i in range(n)]
ruiseki = list(itertools.accumulate(lis))
ruiseki = [x % k for x in ruiseki]
counter = defaultdict(int)
ans = 0
for (i, x) in enumerate(ruiseki):
    ans += counter[x]
    counter[x] += 1
    if i >= k - 1:
        counter[ruiseki[i - k + 1]] -= 1
print(ans)
