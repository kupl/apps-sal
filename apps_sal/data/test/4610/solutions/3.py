from collections import Counter

n, k = list(map(int, input().split()))
ctr = Counter(list(map(int, input().split())))

aa = sorted(list(ctr.items()), key=lambda x: x[1])
if len(aa) <= k:
    print((0))
else:
    print((sum([x[1] for x in aa[:len(aa) - k]])))

