from collections import *
(c, r) = (Counter(), Counter())
(n, k) = list(map(int, input().split()))
ans = []
for i in range(k):
    (i, j) = list(map(int, input().split()))
    (c[i], r[j]) = (1, 1)
    (li, lj) = (len(c), len(r))
    ans.append(n * n - li * n - lj * n + li * lj)
print(*ans)
