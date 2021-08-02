from heapq import heappush, heappop


N, K, *td = list(map(int, open(0).read().split()))
sushis = [(d, t) for t, d in zip(*[iter(td)] * 2)]
sushis.sort(reverse=True)

pq = []
cnt = [0] * (N + 1)
base, x = 0, 0
for d, t in sushis[:K]:
    base += d
    if cnt[t] > 0:
        heappush(pq, (d, t))
    elif cnt[t] == 0:
        x += 1
    cnt[t] += 1
ans = base + x * x

for d, t in sushis[K:]:
    if not pq:
        break
    if cnt[t] > 0:
        continue

    _d, _t = heappop(pq)
    cnt[_t] -= 1
    cnt[t] += 1
    x += 1
    base += d - _d
    ans = max(ans, base + x * x)

print(ans)
