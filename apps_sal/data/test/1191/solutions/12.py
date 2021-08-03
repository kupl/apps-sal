import heapq
n, k = tuple([int(x) for x in input().split(' ')])
p = list([int(x) for x in input().split(' ')])
c = list([int(x) for x in input().split(' ')])
out = [i for i in c]
#t = [(p[i], c[i]) for i in range(n)]
t = [(p[i], i) for i in range(n)]
kbest = []
# print(t)
t.sort()
# print(t)
prev = 0
i = 0
while i < len(t):
    j = i
    while j < len(t) and t[j][0] == t[i][0]:
        out[t[j][1]] += sum(kbest)
        j += 1
    while i < j:
        heapq.heappush(kbest, c[t[i][1]])
        if len(kbest) > k:
            heapq.heappop(kbest)
        i += 1
"""
import bisect
for i in range(n):
    tp = (p[i], -1)
    it = bisect.bisect_left(t, tp)
    #print(it)
    aux = [tup[1] for tup in t[:it]]
    aux.sort()
    out[i] += sum(aux[-k:])
"""
print(' '.join([str(x) for x in out]))
