import heapq as hq
from collections import defaultdict as ddict
import sys
readline = sys.stdin.readline
(N, Q) = list(map(int, readline().split()))
NN = 2 * 10 ** 5
infants = [None] * (N + 1)
kinda = [[] for i in range(NN + 1)]
for i in range(N):
    (a, b) = list(map(int, readline().split()))
    infants[i + 1] = [a, b]
    hq.heappush(kinda[b], (-a, i + 1))
all_kinda = []
for i in range(len(kinda)):
    if kinda[i]:
        hq.heappush(all_kinda, (-1 * kinda[i][0][0], i))


def search_max_rate_from_kinda(x):
    q = kinda[x]
    while q:
        (rate, infant_id) = q[0]
        if infants[infant_id][1] != x:
            hq.heappop(q)
        else:
            return -rate
    return -1


for i in range(Q):
    (target, new_kinda_id) = list(map(int, readline().split()))
    (rate, old_kinda_id) = infants[target]
    infants[target][1] = new_kinda_id
    hq.heappush(kinda[new_kinda_id], (-rate, target))
    old_kinda_rate = search_max_rate_from_kinda(old_kinda_id)
    if old_kinda_rate != -1:
        hq.heappush(all_kinda, (old_kinda_rate, old_kinda_id))
    new_kinda_rate = search_max_rate_from_kinda(new_kinda_id)
    if new_kinda_rate != -1:
        hq.heappush(all_kinda, (new_kinda_rate, new_kinda_id))
    while all_kinda:
        (weakest_rate, kinda_id) = all_kinda[0]
        current_max_rate = search_max_rate_from_kinda(kinda_id)
        if weakest_rate != current_max_rate:
            hq.heappop(all_kinda)
        else:
            print(weakest_rate)
            break
