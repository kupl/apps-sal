from collections import defaultdict
from heapq import heappop, heappush
(N, K) = map(int, input().split())
TD = []
for _ in range(N):
    TD.append(tuple(map(int, input().split())))
TD.sort(key=lambda x: x[1], reverse=True)
D = defaultdict(list)
T = [0] * (N + 1)
H = []
ans = [0]
for (i, td) in enumerate(TD):
    (t, d) = (td[0], td[1])
    if i == K:
        break
    T[t] += 1
    D[t].append(d)
    ans[0] += d
    if T[t] >= 2:
        heappush(H, (D[t].pop(), t))
        T[t] -= 1
cnt = sum((1 for c in T if c >= 1))
ans[0] += cnt ** 2
for i in range(K, N):
    if H:
        (t1, d1) = TD[i]
        if T[t1] == 0:
            (d2, t2) = heappop(H)
            ans.append(ans[-1] + d1 - d2 + 2 * cnt + 1)
            cnt += 1
            T[t1] += 1
    else:
        break
print(max(ans))
