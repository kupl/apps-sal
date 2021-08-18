import heapq
N, K = map(int, input().split())
que = []
for i in range(N):
    t, d = map(int, input().split())
    que.append((t, d))

que.sort(key=lambda x: -x[1])
NOW = que[:K]

N_set = set()

sums = 0

cnt = [0 for i in range(N + 1)]
ng, ok, sub = [], [], []
heapq.heapify(ng)
heapq.heapify(ok)
heapq.heapify(sub)

for index, value in NOW:
    sums += value
    cnt[index] += 1
    heapq.heappush(ng, (value, index))
    N_set.add(index)
while ng:
    value, index = heapq.heappop(ng)
    if cnt[index] > 1:
        heapq.heappush(ok, (value, index))
        cnt[index] -= 1
    elif cnt[index] == 1:
        heapq.heappush(sub, (value, index))

ng = sub


S = len(N_set)
ans = S**2 + sums


for i in range(K, N):
    taste, value = que[i]
    if taste in N_set:
        pass
    else:
        if ok:
            min_value, m_taste = heapq.heappop(ok)
            sums -= min_value
            sums += value
            S += 1
            cnt[taste] += 1
            N_set.add(taste)
            cnt[m_taste] -= 1
            heapq.heappush(ng, (value, taste))
            ans = max(ans, S**2 + sums)

print(ans)
