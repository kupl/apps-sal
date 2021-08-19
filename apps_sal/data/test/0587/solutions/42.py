import heapq
(N, K) = map(int, input().split())
TD = [tuple(map(int, input().split())) for i in range(N)]
TD.sort(key=lambda x: x[1])
hq = []
heapq.heapify(hq)
selected = set()
ans = 0
for _ in range(K):
    (t, d) = TD.pop()
    if t in selected:
        heapq.heappush(hq, d)
    else:
        selected.add(t)
    ans += d
ans += len(selected) ** 2
tmp = ans
while TD:
    (t, d) = TD.pop()
    if t in selected:
        continue
    selected.add(t)
    if len(hq) == 0:
        break
    tmp -= heapq.heappop(hq)
    tmp += d
    tmp += len(selected) * 2 - 1
    ans = max(ans, tmp)
print(ans)
