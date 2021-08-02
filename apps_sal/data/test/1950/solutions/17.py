import heapq
n = int(input())
a = list(map(int, input().split()))

if n % 2 == 0:
    a.append(0)


heapq.heapify(a)
ans = 0
while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    z = heapq.heappop(a)
    ans += x + y + z
    heapq.heappush(a, x + y + z)
print(ans)
