import sys
from collections import Counter
mod = 998244353

n = int(input())
div_n = pow(n, mod - 2, mod)
wants = []
cnt = Counter()
for a in (list(map(int, l.split())) for l in sys.stdin):
    wants.append(a[1:])
    cnt.update(a[1:])

ans = 0

for i in range(n):
    prob = div_n * pow(len(wants[i]), mod - 2, mod) * div_n % mod
    for x in wants[i]:
        ans = (ans + prob * cnt[x]) % mod

print(ans)
