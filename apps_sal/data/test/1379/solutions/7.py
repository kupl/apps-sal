import heapq
n, m, d = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = []
a = [(x, i) for i, x in enumerate(a)]
a.sort()
heap = []
day = 0
for b, i in a:
    found = False
    if len(heap) > 0:
        if heap[0][0] + d < b:
            heapq.heappush(heap, (b, i, heap[0][2]))
            ans.append(heapq.heappop(heap))
            found = True
    if not found:
        heapq.heappush(heap, (b, i, day + 1))
        day += 1
for t in heap:
    ans.append(t)
idx = [0] * n
print(day)
for i in range(len(ans)):
    idx[ans[i][1]] = ans[i][2]
for i in idx:
    print(i, end=' ')
