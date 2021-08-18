
import heapq
N, C = map(int, input().split())
endq = [[] for i in range(C)]
for i in range(C):
    heapq.heapify(endq[i])
progs = [None] * N
for i in range(N):
    s, t, c = map(int, input().split())
    progs[i] = [s, t, c - 1]

progs = sorted(progs, key=lambda x: x[0])

ans = 0
cur = 0

for i in range(N):
    s, t, c = progs[i]
    while endq[c]:
        endt = heapq.heappop(endq[c])
        if endt <= s:
            cur -= 1
        else:
            heapq.heappush(endq[c], endt)
            break

    for endc in range(C):
        if endc == c:
            continue
        while endq[endc]:
            endt = heapq.heappop(endq[endc])
            if endt < s:
                cur -= 1
            else:
                heapq.heappush(endq[endc], endt)
                break
    cur += 1
    heapq.heappush(endq[c], t)
    if cur > ans:
        ans = cur

print(ans)
