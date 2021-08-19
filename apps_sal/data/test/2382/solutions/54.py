from collections import Counter
n = int(input())
a = [int(item) for item in input().split()]
cnt = Counter(a)
key_num = len(cnt.keys())
rank = [0] * key_num
keys = list(cnt.keys())
keys.sort(reverse=True)
for (i, key) in enumerate(keys):
    rank[i] = cnt[key]
cur = [0] * key_num
cur[0] = 1
for i in range(n):
    tmp = cur[:]
    free = 0
    for j in range(key_num):
        if rank[j] > cur[j] and free > 0:
            if cur[j] + free > rank[j]:
                free -= rank[j] - cur[j]
                cur[j] = rank[j]
            else:
                cur[j] += free
                free = 0
        free += tmp[j]
if sum(cur) == 2 ** n:
    print('Yes')
else:
    print('No')
