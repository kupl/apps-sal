import heapq
n, m = list(map(int, input().split()))
byte = [[] for _ in range(100001)]

for _ in range(n):
    a, b = list(map(int, input().split()))
    byte[a].append(b)
search = []
day = 1
ans = 0
while day - 1 != m:
    for b in byte[day]:
        heapq.heappush(search, -b)
    if not search:
        day += 1
        continue
    tmp = -heapq.heappop(search)
    ans += tmp
    day += 1

print(ans)
