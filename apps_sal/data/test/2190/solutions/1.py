from collections import defaultdict
import math
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
hm = defaultdict(int)
for i in range(n):
    x = 2
    t = []
    t1 = []
    y = a[i]
    while x <= math.sqrt(a[i]):
        if a[i] % x == 0:
            c = 0
            while y % x == 0:
                y = y // x
                c += 1
            if c % k > 0:
                t.append((x, c % k))
                t1.append((x, k - c % k))
        x += 1
    if y > 1:
        t.append((y, 1 % k))
        t1.append((y, k - 1 % k))
    ans += hm[tuple(t1)]
    hm[tuple(t)] += 1
print(ans)
