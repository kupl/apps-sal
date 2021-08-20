from collections import defaultdict as dd
n = int(input())
a = [int(x) for x in input().split()]
d = dd(int)
for i in a:
    d[i] += 1
(cnt, ans) = (0, 10000000)
for i in d:
    if d[i] >= 2:
        cnt += 1
if cnt == 0:
    print(0)
else:
    for i in range(n):
        d2 = dd(int)
        ct = 0
        for j in range(i, n):
            d2[a[j]] += 1
            if d2[a[j]] == d[a[j]] - 1 and d[a[j]] >= 2:
                ct += 1
            if ct == cnt:
                ans = min(ans, abs(j - i + 1))
    print(ans)
