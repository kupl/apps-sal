import sys
import collections

n, k = list(map(int, input().split()))
a = list(map(int, sys.stdin.readline().split()))
ct = collections.defaultdict(int)
l, longest, numbers = 0, 0, 0
for r in range(n):
    ct[a[r]] += 1
    if ct[a[r]] == 1:
        numbers += 1
    while numbers > k:
        ct[a[l]] -= 1
        if ct[a[l]] == 0:
            numbers -= 1
        l += 1
    if r - l + 1 > longest:
        longest = r - l + 1
        ans = (l + 1, r + 1)
print('%d %d' % (ans))
