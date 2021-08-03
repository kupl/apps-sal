from collections import Counter
from bisect import bisect_left
from math import gcd
n = int(input())
a = sorted(map(int, input().split()), reverse=True)

m = [[-1] * n for _ in range(n)]
ans = [-1] * n


c = Counter(a)
i = 0
j = n - 1

for i in range(n * n):
    if c[a[i]] == 0:
        continue

    ans[j] = m[j][j] = a[i]

    c[a[i]] -= 1

    for k in range(j + 1, n):
        m[j][k] = m[k][j] = gcd(ans[j], ans[k])
        c[m[j][k]] -= 1
        c[m[k][j]] -= 1

    j -= 1


print(*ans)
