import heapq

n, m = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[0], x[1]))

q = []
ans = 0
for i in range(1, m+1):
    while ab and ab[-1][0] == i:
        a, b = ab.pop()
        heapq.heappush(q, -b)
    if q:
        ans -= heapq.heappop(q)
print(ans)
