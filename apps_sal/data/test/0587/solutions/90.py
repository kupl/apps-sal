from collections import defaultdict
from heapq import heappop, heappush
(N, K) = list(map(int, input().split()))
TD = []
for _ in range(N):
    TD.append(tuple(map(int, input().split())))
TD.sort(key=lambda x: x[1], reverse=True)
TD += [(TD[-1][0], 0)]
D = defaultdict(list)
T = [0] * N
H = []
ans = [0]
for i in range(K):
    (t, d) = TD[i]
    T[t - 1] += 1
    D[t].append(d)
    ans[0] += d
cnt = sum((1 for c in T if c >= 1))
ans[0] += cnt ** 2
for (t, d) in TD:
    if T[t - 1] >= 2:
        heappush(H, (D[t].pop(), t))
        T[t - 1] -= 1
for i in range(K, N):
    if H:
        (t1, d1) = TD[i]
        (d2, t2) = heappop(H)
        if T[t1 - 1] == 0:
            ans.append(ans[-1] + d1 - d2 + 2 * cnt + 1)
            cnt += 1
            T[t1 - 1] += 1
        else:
            heappush(H, (d2, t2))
print(max(ans))
