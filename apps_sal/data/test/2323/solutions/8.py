from bisect import bisect
from collections import Counter
n = int(input())
ns_ = sorted(map(int, input().split()))
diffs = [b - a for (a, b) in zip(ns_, ns_[1:])]
ns = set(ns_)
cnt = Counter(diffs)
cnt.pop(0, None)
sck = sorted(cnt.keys())
remain = [len(ns)]
for k in sck:
    remain.append(remain[-1] - cnt[k])
lastat = [0, *sck]
ans = [remain[0]]
for i in range(len(cnt)):
    ans.append(ans[-1] + remain[i + 1] + remain[i] * (lastat[i + 1] - lastat[i] - 1))
q = int(input())
out = []
for _ in range(q):
    (ll, r) = list(map(int, input().split()))
    x = r - ll
    at = bisect(lastat, x) - 1
    out.append(ans[at] + remain[at] * (x - lastat[at]))
print(' '.join(map(str, out)))
