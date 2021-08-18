from collections import defaultdict
from heapq import heappush, heappop
N, K, *L = map(int, open(0).read().split())
dic = defaultdict(list)
ls = []
for i, (t, d) in enumerate(zip(*[iter(L)] * 2)):
    dic[t].append(d)
    heappush(ls, (-d, t))
S = set()
pre = []
ans = 0
num = 0
for i in range(K):
    d, t = heappop(ls)
    ans -= d
    if t not in S:
        num += 1
        S.add(t)
    else:
        heappush(pre, -d)

ans += num * num
if pre == []:
    print(ans)
    return
m = ans
for i in range(N - K):
    d, t = heappop(ls)
    if t in S:
        continue
    S.add(t)
    m -= heappop(pre)
    m += -d + 2 * num + 1
    num += 1
    ans = max(ans, m)
    if pre == []:
        break
print(ans)
