from collections import defaultdict
import heapq
N = int(input())
alist = list(map(int, input().split()))
adic = defaultdict(int)
for a in alist:
    adic[a] += 1
hq = []
for (k, b) in adic.items():
    heapq.heappush(hq, (-b, k))
cnt = 0
while True:
    (mf, n) = heapq.heappop(hq)
    if mf == -1:
        break
    elif mf <= -3:
        heapq.heappush(hq, (mf + 2, n))
        cnt += 1
    else:
        (mf2, n2) = heapq.heappop(hq)
        if mf2 == -1:
            cnt += 1
            break
        else:
            heapq.heappush(hq, (mf + 1, n))
            cnt += 1
print(N - 2 * cnt)
