import heapq as he
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x * -1, a))
he.heapify(a)
for i in range(m):
    he.heappush(a, he.heappop(a) * -1 // 2 * -1)
print(sum(a) * -1)
