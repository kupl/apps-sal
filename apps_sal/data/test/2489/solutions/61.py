import collections
n = int(input())
a = sorted([int(i) for i in input().split()])
cnt = collections.Counter(a)
max_i = a[-1] + 1
for i in a:
  if cnt[i] >= 2:
    del cnt[i]
  for j in range(i*2, max_i, i):
    del cnt[j]
print(len(cnt))
