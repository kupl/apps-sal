import heapq
(n, m) = map(int, input().split())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))
ab.sort()
ans = 0
num = 0
queue = []
heapq.heapify(queue)
for i in range(1, m + 1):
    if num < n:
        while ab[num][0] <= i:
            heapq.heappush(queue, [-ab[num][1], ab[num][0]])
            num += 1
            if num == n:
                break
    if len(queue):
        temp = heapq.heappop(queue)
        ans += -temp[0]
print(ans)
