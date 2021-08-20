import math
from collections import Counter
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
prev = Counter()
for x in a:
    sig = []
    p = 2
    while p <= math.sqrt(x):
        cnt = 0
        while x % p == 0:
            cnt += 1
            x = x // p
        cnt = cnt % k
        if cnt > 0:
            sig.append((p, cnt))
        p += 1
    if x > 1:
        sig.append((x, 1))
    com_sig = []
    for (p, val) in sig:
        com_sig.append((p, (k - val) % k))
    ans += prev[tuple(sig)]
    prev[tuple(com_sig)] += 1
print(ans)
