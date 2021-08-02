import heapq
N, K = map(int, input().split())
td = [list(map(int, input().split())) for i in range(N)]
td.sort(key=lambda x: -x[1])
sumn = [[] for i in range(N)]
for i in range(N):
    heapq.heapify(sumn[i])
ans = 0
kind = {}
for t, d in td[:K]:
    if t not in kind:
        kind[t] = 1
    else:
        kind[t] += 1
    heapq.heappush(sumn[t - 1], d)
kinds = len(kind)
ans = sum(sum(i) for i in sumn)
ans1 = ans + kinds**2
rem = td[K:]
nex = 0
candel = []
heapq.heapify(candel)
for k, v in kind.items():
    for i in range(v - 1):
        heapq.heappush(candel, heapq.heappop(sumn[k - 1]))
if candel:
    qd = heapq.heappop(candel)
    while K + nex < N:
        if td[K + nex][0] not in kind:
            kind[td[K + nex][0]] = 1
            kinds += 1
            ans = ans - qd + td[K + nex][1]
            ans1 = max(ans1, ans + kinds**2)
            nex += 1
            if candel:
                qd = heapq.heappop(candel)
            else:
                break
        else:
            nex += 1
print(ans1)
