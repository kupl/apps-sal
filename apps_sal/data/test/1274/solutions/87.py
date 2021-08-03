import heapq
n, m = map(int, input().split())
b_list = [[] for _ in range(10**5 + 10)]

for i in range(n):
    a, b = map(int, input().split())
    b_list[a].append(-b)

candy = []
heapq.heapify(candy)
ans = 0
for i in range(1, m + 1):
    for j in b_list[i]:
        heapq.heappush(candy, j)
    if candy:
        ans += (-1 * heapq.heappop(candy))

print(ans)
