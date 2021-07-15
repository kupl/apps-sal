# D - Various Sushi
import sys
from collections import defaultdict
import heapq

readline = sys.stdin.readline

dd = defaultdict(list)
N, K = list(map(int, readline().split()))
for i in range(N):
    t, d = list(map(int, readline().split()))
    heapq.heappush(dd[t], d*-1)

dd = list(dd.values())
dd.sort()

ans = 0
fix = 0
var = []
len_var = 0
sum_var = 0
tmp_max = 0

for i in range(min(K, len(dd))):
    fix += heapq.heappop(dd[i]) * -1
    for _ in range(len(dd[i])):
        tmp = heapq.heappop(dd[i]) * -1
        heapq.heappush(var, tmp)
        len_var += 1
        sum_var += tmp
    while len_var > K-(i+1) and len_var > 0:
        del_var = heapq.heappop(var)
        len_var -= 1
        sum_var -= del_var
    if len_var == K-(i+1):
        ans = max(ans , fix+sum_var + (i+1)**2)

print(ans)

