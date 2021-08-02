from itertools import accumulate
from collections import defaultdict

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

acc = [0] + list(accumulate(a))
sm = [(e - i) % k for i, e in enumerate(acc)]

d = defaultdict(int)
ans = 0
for r in range(1, n + 1):
    if r - k >= 0:
        e = sm[r - k]
        d[e] -= 1

    e = sm[r - 1]
    d[e] += 1

    e = sm[r]
    ans += d[e]

print(ans)
