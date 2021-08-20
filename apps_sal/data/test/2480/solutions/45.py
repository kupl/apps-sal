from collections import defaultdict
from bisect import bisect_right
(n, k) = list(map(int, input().split()))
alst = list(map(int, input().split()))
dd = defaultdict(list)
dd[0].append(0)
total = 0
for (i, num) in enumerate(alst, start=1):
    total += num
    total %= k
    app = total - i
    app %= k
    dd[app].append(i)
ans = 0
for (_, lst) in list(dd.items()):
    for (i, num) in enumerate(lst):
        num2 = num + k - 1
        pos = bisect_right(lst, num2)
        ans += pos - i - 1
print(ans)
