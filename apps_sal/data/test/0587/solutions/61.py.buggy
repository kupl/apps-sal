from heapq import heappop, heappush
import sys
input = sys.stdin.readline
hq = []
n, k = list(map(int, input().split()))
for i in range(n):
    t, d = list(map(int, input().split()))
    heappush(hq, (-d, t))
D = 0
dic = {}
got = []
for i in range(k):
    r = heappop(hq)
    got.append(r)
    if r[1] in dic:
        dic[r[1]] += 1
    else:
        dic[r[1]] = 1
    D += -r[0]
ans = D + len(dic)**2

while hq:
    while got:
        p = got.pop()
        if dic[p[1]] > 1:
            dic[p[1]] -= 1
            D -= -p[0]
            break
    if len(got) == 0:
        print(ans)
        return

    r = heappop(hq)
    got.append(r)
    if r[1] in dic:
        dic[r[1]] += 1
    else:
        dic[r[1]] = 1
    D += -r[0]
    ans = max(D + len(dic)**2, ans)
print(ans)
