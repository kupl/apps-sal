import collections
N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=False)
cnt = collections.Counter(a)
m = max(a) + 1
for i in a:
    if cnt[i] >= 2:
        del cnt[i]
    for j in range(i * 2, m, i):
        del cnt[j]
print(len(cnt.keys()))
