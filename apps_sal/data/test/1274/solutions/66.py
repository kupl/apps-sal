# m-1日目は、a<=1で最大報酬のアルバイトをやる
# m-2日目は、a<=2で最大報酬のアルバイトをやる（ただし、m-1日目に選択したアルバイトを除く）
# 以下この要領で後ろから決めていく
from collections import defaultdict
from heapq import heapify, heappush, heappop

n, m = list(map(int, input().split()))
d = defaultdict(list)
for _ in range(n):
    a, b = list(map(int, input().split()))
    d[a].append(b)

L = []
heapify(L)

ans = 0
for remain in range(1, m + 1):
    for reward in d[remain]:
        heappush(L, -reward)
    if len(L):
        ans -= heappop(L)

print(ans)
