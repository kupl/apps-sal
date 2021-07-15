n, k = list(map(int, input().split()))

from collections import defaultdict

nums = list(map(int, input().split()))

cc = defaultdict(int)
aa = defaultdict(list)

for num in nums:
    o = num
    i = 0
    while o != 0:
        cc[o] += 1
        aa[o].append(i)
        i += 1
        o //= 2

candidates = [name for name, count in list(cc.items()) if count >= k]

m = float('inf')

for name in candidates:
    m = min(m, sum(sorted(aa[name])[:k]))

print(m)

