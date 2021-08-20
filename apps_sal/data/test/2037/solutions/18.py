from heapq import heappush, heappop
from collections import defaultdict
(num_difs, num_probs) = [int(x) for x in input().split()]
probs = [int(x) - 1 for x in input().split()]


def root_not_uptodate(heap):
    (val, idx) = heap[0]
    return dif_counts[idx] != val


is_round = [False for _ in range(num_probs)]
heap = [(0, idx) for idx in range(num_difs)]
dif_counts = defaultdict(int)
num_held = 0
for (i, dif) in enumerate(probs):
    dif_counts[dif] += 1
    heappush(heap, (dif_counts[dif], dif))
    while heap and root_not_uptodate(heap):
        heappop(heap)
    if heap and heap[0][0] - num_held > 0:
        num_held += 1
        is_round[i] = True
print(''.join(('1' if is_r else '0' for is_r in is_round)))
