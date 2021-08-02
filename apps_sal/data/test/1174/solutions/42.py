import heapq

# 優先度付きキューは「最も値が小さいもの」を出すことに注意

prio = []

n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

for num in nums:
    heapq.heappush(prio, -num)

for i in range(m):
    temp = heapq.heappop(prio)
    heapq.heappush(prio, -((-temp) // 2))

print((-sum(prio)))
