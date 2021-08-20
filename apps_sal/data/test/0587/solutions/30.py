import heapq
(n, k) = list(map(int, input().split()))
L = []
for i in range(n):
    (t, d) = list(map(int, input().split()))
    L.append([d, t])
L.sort()
ans = []
cur = [0] * n
heap = []
var = 0
for i in range(k):
    if cur[L[n - i - 1][1] - 1] == 0:
        ans.append(L[n - i - 1][0])
        cur[L[n - i - 1][1] - 1] = 1
        var += 1
    else:
        heapq.heappush(heap, L[n - i - 1])
temp = 0
for i in range(len(ans)):
    temp += ans[i]
for i in range(len(heap)):
    temp += heap[i][0]
temp += var ** 2
now = temp
for i in range(n - k):
    if len(heap) != 0:
        a = heapq.heappop(heap)
        if cur[L[n - k - i - 1][1] - 1] == 0:
            ans.append(L[n - k - i - 1][0])
            cur[L[n - k - i - 1][1] - 1] = 1
            now -= var ** 2
            now -= a[0]
            var += 1
            now += var ** 2
            now += L[n - k - i - 1][0]
            temp = max(temp, now)
        else:
            heapq.heappush(heap, a)
print(temp)
