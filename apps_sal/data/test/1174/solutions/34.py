import heapq
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x * -1, a))
heapq.heapify(a)
for i in range(m):
    tmp = heapq.heappop(a)
    tmp /= 2
    heapq.heappush(a, tmp)
ans = 0
for aa in a:
    ans += aa // -1
print(int(ans))
