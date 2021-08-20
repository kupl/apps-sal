from collections import Counter
import heapq
n = int(input())
sc = Counter()
for x in range(n):
    s = input()
    sc.update([s])
max_num = sc.most_common()[0][1]
q = []
for v in list(sc.items()):
    if v[1] == max_num:
        heapq.heappush(q, v[0])
for _ in range(len(q)):
    print(heapq.heappop(q))
