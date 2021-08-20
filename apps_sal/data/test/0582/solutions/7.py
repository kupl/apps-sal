from heapq import heapify, heappop, heappush
import collections
n = int(input())
a = [int(i) for i in input().split(' ')]
t = [int(i) for i in input().split(' ')]
l = collections.defaultdict(list)
at = [[a[i], t[i]] for i in range(n)]
at.sort(key=lambda x: x[0])
for (aa, tt) in at:
    l[aa].append(tt)
res = 0
q = sorted(l.keys())[::-1]
tmp = []
heapify(tmp)
sums = 0
while q:
    i = q.pop()
    if len(l[i]) == 1 and (not tmp):
        continue
    else:
        for ll in l[i]:
            heappush(tmp, -ll)
            sums += ll
        idx = i
        while tmp and (q and idx + 1 != q[-1] or not q):
            p = -heappop(tmp)
            res += sums - p
            sums -= p
            idx += 1
        if tmp:
            p = -heappop(tmp)
            res += sums - p
            sums -= p
            if not q:
                q.append(idx + 1)
print(res)
