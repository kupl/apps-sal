from collections import defaultdict
from heapq import heappop, heappush
(N, K) = map(int, input().split())
TD = []
for _ in range(N):
    TD.append(tuple(map(int, input().split())))
TD.sort(key=lambda x: x[1], reverse=True)
TD += [(TD[-1][0], 0)]
D = defaultdict(list)
T = [0] * N
H = []
ans = 0
for i in range(K):
    (t, d) = TD[i]
    T[t - 1] += 1
    D[t].append(d)
    ans += d
cnt = sum((1 for c in T if c >= 1))
ans += cnt ** 2
for t in range(1, N + 1):
    if T[t - 1] >= 2:
        heappush(H, (D[t].pop(), t))
        T[t - 1] -= 1
for i in range(K, N):
    if H:
        (t1, d1) = TD[i]
        (d2, t2) = heappop(H)
        if T[t1 - 1] == 0 and d1 - d2 + 2 * cnt + 1 >= 0:
            ans += d1 - d2 + 2 * cnt + 1
            cnt += 1
            T[t1 - 1] += 1
            if T[t2 - 1] >= 2:
                T[t2 - 1] -= 1
            if T[t2 - 1] >= 2:
                heappush(H, (D[t2].pop(), t2))
        else:
            heappush(H, (d2, t2))
ans2 = 0
T2 = [0] * N
D2 = []
cnt2 = 0
for (t, d) in TD:
    if cnt2 < K:
        if T2[t - 1]:
            D2.append(d)
        else:
            T2[t - 1] = 1
            ans2 += d
            cnt2 += 1
ans2 += sum(D2[:K - cnt2]) + sum(T2) ** 2
print(max(ans, ans2))
