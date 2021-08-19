import collections
import bisect
n = int(input())
cnt = collections.defaultdict(list)
dat = list(map(int, input().split()))
buf = []
for i in range(n):
    cnt[i - dat[i]].append(i)
# print(buf)
res = 0
for i in range(n):
    x = i + dat[i]
    if x in cnt:
        res += len(cnt[x]) - bisect.bisect_left(cnt[x], x)
print(res)
